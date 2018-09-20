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
# trich khung diem
img = cv2.imread(args["query"])
x = fac.find(img)
img1 = fac.rotateAndCrop(x,img)
img1 = fac.remove_Border(img1)

# Nhan dien diem
text = pytesseract.image_to_string(img1,config='-psm 6')
diem = ""
for i in range(len(text)):
	if (text[i] >= '0' and text[i] <= '9') or text[i] == '.' or text[i] == ',':
		diem += text[i]
print("diem = ", diem)
#cv2.imwrite('diem.png',img1)
# cv2.imshow('diem',mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()