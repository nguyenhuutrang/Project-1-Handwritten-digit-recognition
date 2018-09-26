import cv2
import find_and_crop as fac
import argparse
import pytesseract


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
args = vars(ap.parse_args())

# working
# trich khung diem va khung MSSV
img = cv2.imread(args["query"])
x = fac.find(img)
img1 = fac.rotateAndCrop(x,img)
imgMSSV,imgDiem = fac.remove_Border(img1)

# cv2.imshow('MSSV',imgMSSV)
# cv2.imshow('DIEM',imgDiem)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Nhan dien diem va mssv
MSSV = pytesseract.image_to_string(imgMSSV,config='-psm 6')
DIEM = pytesseract.image_to_string(imgDiem,config='-psm 6')
#print(MSSV ,'-->', DIEM)

# Loại bỏ các khoảng trắng thừa và các kí tự lạ
mssv = fac.xuLyText(MSSV)
diem = fac.xuLyText(DIEM)
print("MSSV: ",mssv, "--> Diem: ",diem)
