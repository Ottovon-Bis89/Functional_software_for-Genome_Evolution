
# import cv2
# import numpy as np
# from PIL import Image
# import os

# # Directory containing your image files (chr1.png, chr2.png, etc.)
# image_dir = "/home/22204911/Documents/new_result/1_2/"


# # Get a list of image files in the directory
# image_files = os.listdir(image_dir)

# # Filter and sort the image files in descending order
# valid_image_files = [file for file in image_files if file.startswith('chr') and file.endswith('.jpeg')]
# sorted_image_files = sorted(valid_image_files, key=lambda x: -int(x.split('chr')[1].split('.')[0]))

# # Initialize an empty list to store the loaded images
# images = []

# # Load and append the images in descending order
# for image_file in sorted_image_files:
#     image_path = os.path.join(image_dir, image_file)
#     image = cv2.imread(image_path)
#     images.append(image)

# # Stack the images horizontally (change axis to 0 for vertical stacking)
# combined_image = np.concatenate(images, axis=0)

# # Display or save the combined image as needed
# cv2.imshow('Combined Image', combined_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # If you want to save the combined image as a file:
# # output_filename = os.path.splitext(image_file)[0] + '.jpeg'

# cv2.imwrite('combined_image.png', combined_image)




import os
from PIL import Image

folder_a = "/home/22204911/Documents/new_result/HiC_img"
folder_b = "/home/22204911/Documents/new_result/R-H_mapped"
output_folder = "/home/22204911/Documents/new_result/new_link.out"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all image files in folder A
image_files_a = [f for f in os.listdir(folder_a) if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))]

# List all image files in folder B
image_files_b = [f for f in os.listdir(folder_b) if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))]

# Loop through each image file in folder A
for img_file_a in image_files_a:
    # Open the image in folder A
    with Image.open(os.path.join(folder_a, img_file_a)) as image_a:
        # Loop through each image file in folder B
        for img_file_b in image_files_b:
            # Open the file in folder B
            with Image.open(os.path.join(folder_b, img_file_b)) as image_b:
                # # Concatenate the images vertically
                concatenated_image = Image.new('RGB', (max(image_a.width, image_b.width), image_a.height + image_b.height))
                concatenated_image.paste(image_b, (0, 0))
                concatenated_image.paste(image_a, (0, image_b.height))

                
                # Save the concatenated image to the output folder
                output_filename = f"{os.path.splitext(img_file_a)[0]}_{os.path.splitext(img_file_b)[0]}.jpeg"
                concatenated_image.save(os.path.join(output_folder, output_filename))
                


print("Concatenation complete.")

