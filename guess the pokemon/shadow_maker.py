from PIL import Image, ImageOps
import os

# Define the path to the input and output folders
input_path = "images"
output_path = "shadowed_images"

# Create the output folder if it doesn't already exist
if not os.path.exists(output_path):
    os.mkdir(output_path)

# Define the filter settings
desaturation_factor = 0.5
brightness_factor = 0.5
outline_size = 2
outline_color = "black"

# Loop through all JPEG files in the input folder
for filename in os.listdir(input_path):
    if filename.endswith(".jpg"):
        # Open the image and apply the filter
        input_image = Image.open(os.path.join(input_path, filename))
        filtered_image = ImageOps.colorize(
            ImageOps.autocontrast(input_image, cutoff=10),
            black="black",
            white=(1 - desaturation_factor, 1 - desaturation_factor, 1 - desaturation_factor),
        )
        filtered_image = ImageOps.expand(filtered_image, outline_size, outline_color)
        filtered_image = ImageOps.autocontrast(filtered_image, cutoff=10)
        filtered_image = ImageOps.brightness(filtered_image, brightness_factor)

        # Save the filtered image in the output folder with the same filename
        output_filename = os.path.join(output_path, filename)
        filtered_image.save(output_filename)
