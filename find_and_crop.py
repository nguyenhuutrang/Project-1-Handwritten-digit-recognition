import numpy as np
import cv2

def find(img):
    screenCnt = None
    # chuyển sang ảnh gray là làm mờ
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    gray = cv2.GaussianBlur(gray,(7,7),0)
    
    # Phát hiện các cạnh trong hình
    edges = cv2.Canny(gray,10,250)
    
    # tiến hành lọc bỏ những phần đen nằm giữa các viền trắng
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
    closed = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel)
    
    # Sử dụng find contours để phát hiện khung hình chữ nhật ghi điểm
    _, contours, _ = cv2.findContours(closed.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        if len(approx) == 4:
            screenCnt = approx
            #cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
            break
    return screenCnt

def rotateAndCrop(screenCnt,orig):
    # Xác định tọa độ 4 đỉnh của khung điểm
    pts = screenCnt.reshape(4, 2)
    rect = np.zeros((4, 2), dtype = "float32")

    # Điểm trên cùng bên trái có tổng tọa độ min,
    #  điểm dưới cùng bên phải có tổng tọa độ max
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # Điểm dưới cùng bên trái sẽ có khác biệt nhỏ nhất 
    # trong khi điểm trên cùng bên phải có khác biết lớn nhất
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # Tính toán kích thước của khung điểm
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

    # Lấy giá trị max của width và height để cân chỉnh khung điểm
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))

    # Chuyển đổi góc nhìn , đưa về góc nhìn từ trên xuống
    dst = np.array([
	    [0, 0],
	    [maxWidth - 1, 0],
	    [maxWidth - 1, maxHeight - 1],
	    [0, maxHeight - 1]], dtype = "float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))
    
    cv2.imwrite('diem.png',warp)
    #cv2.imshow('khung diem',warp)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



