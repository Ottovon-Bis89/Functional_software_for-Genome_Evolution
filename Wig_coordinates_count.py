

# Function to read coordinates from a text file and return a set of unique coordinates
def read_coordinates(file_path):
    unique_coordinates = set()
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming the coordinates are on each line separated by whitespace
            coordinates = line.strip().split()
            for coord in coordinates:
                unique_coordinates.add(coord)
    return unique_coordinates

# File paths for your input files
# file_A = "/home/22204911/Documents/chrom_interactions/chrom2_interac_points"
# file_B = "/home/22204911/Documents/chrom_mutations/chrom3_mut_points"

file_A = "/home/22204911/Documents/interaction.wig/chrom1_inter.wig"
file_B = "/home/22204911/Documents/mutation.wig/chrom2_mut.wig"

# Read unique coordinates from both files
unique_coordinates_A = read_coordinates(file_A)
unique_coordinates_B = read_coordinates(file_B)

# Find common coordinates between the two sets
common_coordinates = unique_coordinates_A.intersection(unique_coordinates_B)

# Count the number of unique coordinates in each file and the number of common coordinates
count_unique_coordinates_A = len(unique_coordinates_A)
count_unique_coordinates_B = len(unique_coordinates_B)
count_common_coordinates = len(common_coordinates)

# Print the results
print(f"Number of unique coordinates in file A: {count_unique_coordinates_A}")
print(f"Number of unique coordinates in file B: {count_unique_coordinates_B}")
print(f"Number of common coordinates between the two files: {count_common_coordinates}")



# #Function to read coordinates from a text file and return a list of coordinates
# def read_coordinates(file_path):
#     coordinates = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Assuming the coordinates are on each line separated by whitespace
#             coordinates.extend(line.strip().split())
#     return coordinates

# # File paths for your input files
# file_A = "/home/22204911/Documents/interaction.wig/chrom2_inter.wig"
# file_B =  "/home/22204911/Documents/mutation.wig/chrom4_mut.wig"

# # file_A = "/home/22204911/Documents/chrom_interactions/chrom1_interac_points"
# # file_B = "/home/22204911/Documents/chrom_mutations/chrom5_mut_points"

# # Read coordinates from both files
# coordinates_A = read_coordinates(file_A)
# coordinates_B = read_coordinates(file_B)

# # Count the number of coordinates in each file and the number of common coordinates
# count_coordinates_A = len(coordinates_A)
# count_coordinates_B = len(coordinates_B)
# count_common_coordinates = len(set(coordinates_A) & set(coordinates_B))

# # Print the results
# print(f"Number of coordinates in file A: {count_coordinates_A}")
# print(f"Number of coordinates in file B: {count_coordinates_B}")
# print(f"Number of common coordinates between the two files: {count_common_coordinates}")



# def read_wiggle_file(filename):
#     positions = set()
#     with open(filename, 'r') as file:
#         for line in file:
#             if line.startswith("fixedStep") or line.startswith("variableStep"):
#                 continue
#             parts = line.strip().split()
#             if len(parts) >= 3:
#                 chrom = parts[0]
#                 start = int(parts[1])
#                 positions.add((chrom, start))
#     return positions

# # Read the positions from file A and file B
# positions_A = read_wiggle_file("/home/22204911/Documents/chrom_interactions/chrom1_interac_points")
# positions_B = read_wiggle_file("/home/22204911/Documents/chrom_mutations/chrom2_mut_points")

# # Find the common positions
# common_positions = positions_A.intersection(positions_B)

# # Count the positions in A, B, and both A and B
# count_A = len(positions_A)
# count_B = len(positions_B)
# count_common = len(common_positions)

# print(f"Count of positions in A: {count_A}")
# print(f"Count of positions in B: {count_B}")
# print(f"Count of positions in both A and B: {count_common}")



# import cv2
# import numpy as np

# def count_vertical_bars(image):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply edge detection to detect vertical lines
#     edges = cv2.Canny(gray, 50, 150, apertureSize=3)

#     # Apply a dilation operation to make lines thicker
#     dilated = cv2.dilate(edges, None, iterations=3)

#     # Find contours in the dilated image
#     contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#     # Count the number of vertical bars
#     vertical_bar_count = 0
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         if w > 0.0001 and h >= 10:  # You can adjust the minimum width and height
#             vertical_bar_count += 1

#     return vertical_bar_count

# def find_common_bars(image1, image2):
#     # Count vertical bars in each image
#     vertical_bars_image1 = count_vertical_bars(image1)
#     vertical_bars_image2 = count_vertical_bars(image2)

#     # Combine the two images vertically
#     combined_image = np.vstack((image1, image2))
    

#     # Count vertical bars in the combined image
#     vertical_bars_combined = count_vertical_bars(combined_image)
#     print(vertical_bars_combined)
   

#     # Calculate common bars by subtracting the total vertical bars in the combined image
#     # from the sum of vertical bars in individual images
#     common_bars = vertical_bars_image1 + vertical_bars_image2 - vertical_bars_combined

#     return vertical_bars_image1, vertical_bars_image2, common_bars

# # Load your two images
# image1 = cv2.imread("/home/22204911/Documents/rearrange_Hi-C_point_images/one_and_three/chr1.jpeg")
# image2 = cv2.imread("/home/22204911/Documents/rearrange_Hi-C_point_images/one_and_three/chr3.jpeg")

# # Find the counts of vertical bars and common bars
# vertical_bars_image1, vertical_bars_image2, common_bars = find_common_bars(image1, image2)

# print(f"Vertical bars in image 1: {vertical_bars_image1}")
# print(f"Vertical bars in image 2: {vertical_bars_image2}")
# print(f"Common bars between the two images: {common_bars}")


# import cv2
# import numpy as np

# def count_vertical_bars(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray, 50, 150, apertureSize=3)
#     dilated = cv2.dilate(edges, None, iterations=3)
#     contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     vertical_bars = []
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         if w > 0.5 and h > 10:  # Adjust the minimum width and height as needed
#             vertical_bars.append((x, y, w, h))
    
#     return vertical_bars

# def find_common_bars(image1, image2):
#     # Count vertical bars in each image
#     vertical_bars_image1 = count_vertical_bars(image1)
#     vertical_bars_image2 = count_vertical_bars(image2)

#     # Find common bars that intersect in both images
#     common_bars = []
#     for bar1 in vertical_bars_image1:
#         for bar2 in vertical_bars_image2:
#             x1, y1, w1, h1 = bar1
#             x2, y2, w2, h2 = bar2
#             if (
#                 x1 < x2 + w2 and
#                 x1 + w1 > x2 and
#                 y1 < y2 + h2 and
#                 y1 + h1 > y2
#             ):
#                 common_bars.append(bar1)
#                 break
    
#     return vertical_bars_image1, vertical_bars_image2, common_bars

# # Load your two images
# image1 = cv2.imread("/home/22204911/Documents/rearrange_Hi-C_point_images/one_and_three/chr1.jpeg")
# image2 = cv2.imread("/home/22204911/Documents/rearrange_Hi-C_point_images/one_and_two/chr1.jpeg")

# # Find the counts of vertical bars and common bars
# vertical_bars_image1, vertical_bars_image2, common_bars = find_common_bars(image1, image2)

# print(f"Vertical bars in image 1: {len(vertical_bars_image1)}")
# print(f"Vertical bars in image 2: {len(vertical_bars_image2)}")
# print(f"Common bars between the two images: {len(common_bars)}")


# import cv2

# def count_vertical_bars(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray, 50, 150, apertureSize=3)
#     dilated = cv2.dilate(edges, None, iterations=3)
#     contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     vertical_bars = []
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         if w > 100 and h <300:  # Adjust the minimum width and height as needed
#             vertical_bars.append((x, y, w, h))
    
#     return vertical_bars

# def find_common_bars(image1, image2):
#     # Count vertical bars in each image
#     vertical_bars_image1 = count_vertical_bars(image1)
#     vertical_bars_image2 = count_vertical_bars(image2)

#     # Find common bars that intersect in both images
#     common_bars = []
#     for bar1 in vertical_bars_image1:
#         for bar2 in vertical_bars_image2:
#             x1, y1, w1, h1 = bar1
#             x2, y2, w2, h2 = bar2
#             if (
#                 x1 < x2 + w2 and
#                 x1 + w1 > x2 and
#                 y1 < y2 + h2 and
#                 y1 + h1 > y2
#             ):
#                 common_bars.append(bar1)
#                 break
    
#     return vertical_bars_image1, vertical_bars_image2, common_bars

# # Load your two images
# image1 = cv2.imread("/home/22204911/Documents/rearrange_Hi-C_point_images/one_and_three/chr1.jpeg")
# image2 = cv2.imread("/home/22204911/Documents/rearrange_Hi-C_point_images/one_and_two/chr2.jpeg")

# # Find the counts of vertical bars and common bars
# vertical_bars_image1, vertical_bars_image2, common_bars = find_common_bars(image1, image2)

# print(f"Vertical bars in image 1: {len(vertical_bars_image1)}")
# print(f"Vertical bars in image 2: {len(vertical_bars_image2)}")
# print(f"Common bars between the two images: {len(common_bars)}")



