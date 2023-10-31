


# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('/home/22204911/Documents/new_result/crosslink.annotate1/chr10_chr2.jpeg')  # Replace 'your_image.png' with the path to your image

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Threshold the image to create a binary image
# _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# # Find contours in the binary image
# contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Iterate through the contours and find intersection points along the diameter
# for contour in contours:
#     if len(contour) >= 2:
#         for i in range(len(contour) - 1):
#             point1 = tuple(contour[i][0])
#             point2 = tuple(contour[i + 1][0])
            
#             # Calculate the distance between two points
#             distance = np.linalg.norm(np.array(point1) - np.array(point2))
            
#             if distance < 6:  # Adjust the threshold as needed
#                 x, y = point1
#                 cv2.circle(image, (x, y), 1, (0, 0, 255), -1)  # Mark the point in red

# # Display the marked image
# cv2.imshow('Marked Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the image
image = cv2.imread('/home/22204911/Documents/new_result/crosslink.annotate1/chr10_chr2.jpeg')  # Replace 'your_image.png' with the path to your image

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image
_, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a list to store the intersection points
intersection_points = []

# Iterate through the contours and find intersection points along the diameter
for contour in contours:
    if len(contour) >= 2:
        for i in range(len(contour) - 1):
            point1 = tuple(contour[i][0])
            point2 = tuple(contour[i + 1][0])
            
            # Calculate the distance between two points
            distance = np.linalg.norm(np.array(point1) - np.array(point2))
            
            if distance < 5:  # Adjust the threshold as needed
                intersection_x = (point1[0] + point2[0]) // 2
                intersection_y = (point1[1] + point2[1]) // 2
                intersection_points.append((intersection_x, intersection_y))

# Mark the intersection points with a red dot
for x, y in intersection_points:
    cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

# Display the marked image
cv2.imshow('Marked Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
