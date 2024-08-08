import cv2
import imutils
import numpy as np

# Load Image
image = cv2.imread("shape.jpg")
cv2.imshow("Image", image)
cv2.waitKey(0)

value =100
mat = np.ones(image.shape,dtype = 'uint8')*value
subtract = cv2.subtract(image,mat)
cv2.imshow('subtract',subtract)
cv2.waitKey(0)

# convert the image to grayscale
gray = cv2.cvtColor(subtract, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

blurgray = cv2.GaussianBlur(gray, (15,15), 0)
cv2.imshow("Gray Blur", gray)
cv2.waitKey(0)

# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
thresh = cv2.threshold(blurgray, thresh=127,maxval= 255, type=cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Threshold", thresh)

# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
# loop over the contours
for c in cnts:
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contours", output)
	cv2.waitKey(0)

# draw the total number of contours found in purple
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)