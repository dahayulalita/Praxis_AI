import cv2
import imutils

# image acces
image = cv2.imread("meme.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("acces", image)
cv2.waitKey(0)

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[10:110, 20:200]
cv2.imshow("zoom", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (500, 500))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, 90)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# smoothing an image
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11,11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# drawing on an image
# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (50, 70), (185, 140), (0, 255, 255), 7)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (150, 150), 20, (255, 0, 0), 10)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (0, 0), (300, 300), (0, 255, 255), 5)
cv2.imshow("Line", output)

cv2.line(output, (300, 0), (0, 300), (255, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# draw text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Mark!", (30, 80), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

