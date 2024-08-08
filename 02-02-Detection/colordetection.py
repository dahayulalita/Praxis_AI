import numpy as np
import argparse
import cv2

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image", default="shape.jpg")  # Add a default value
args = vars(ap.parse_args())

# Load the image from the path provided by the argument
image = cv2.imread(args["image"])

if image is None:
    raise ValueError("Image not found or path is incorrect")

# Define the list of boundaries
boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]

# Loop over the boundaries
for (lower, upper) in boundaries:
    # Create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # Find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    # Show the images
    cv2.imshow("Image", np.hstack([image, output]))
    cv2.waitKey(0)

cv2.destroyAllWindows()