
import os
from PIL import Image

folder_a = "/home/von/Documents/ch_seq.image"
folder_b = "/home/von/Documents/ch_mut.image"
output_folder = "/home/von/Documents/ch_seq.out"

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
                # Create a new image with a white background
                concatenated_image = Image.new('RGB', (max(image_a.width, image_b.width), image_a.height + image_b.height), 'white')
                
                # Paste the second image at the top
                concatenated_image.paste(image_b, (0, 0))
                
                # Paste the first image at the bottom
                concatenated_image.paste(image_a, (0, image_b.height))

                # Save the concatenated image to the output folder
                output_filename = f"{os.path.splitext(img_file_a)[0]}_{os.path.splitext(img_file_b)[0]}.jpeg"
                concatenated_image.save(os.path.join(output_folder, output_filename))

print("Concatenation complete.")
