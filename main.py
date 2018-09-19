import cv2
import find_and_crop as fac
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
args = vars(ap.parse_args())

# working
img = cv2.imread(args["query"])
x = fac.find(img)
fac.rotateAndCrop(x,img)