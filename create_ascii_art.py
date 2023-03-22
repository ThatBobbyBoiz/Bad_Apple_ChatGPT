"""
Before running this code, you must have every single frame of
Bad Apple video in a directory. There are many online public code
that are used to extract a video into frames. I would recommend
this one "https://pypi.org/project/videotoframes/"
"""

import os
from PIL import Image

# Define ASCII characters to use
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Set input and output directory paths
input_dir = "{your raw bad apple frames directory}"  #change this
output_dir = "{your modified bad apple frames directory}"  #change this

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all frame files in the input directory and sort them in alphanumeric order
frame_files = os.listdir(input_dir)
frame_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# Loop through each frame file and convert to ASCII art
for i, frame_file in enumerate(frame_files):
    # Open frame file as an image
    frame_path = os.path.join(input_dir, frame_file)
    frame_image = Image.open(frame_path)

    # Resize image to fit in the terminal window
    width, height = frame_image.size
    aspect_ratio = height / width
    new_width = 150 
    new_height = int(aspect_ratio * new_width * 0.244)
    if new_height > 44:
        new_height = 44
        new_width = int(new_height / aspect_ratio / 0.244)
    resized_image = frame_image.resize((new_width, new_height))

    # Convert image to grayscale and get pixel data
    grayscale_image = resized_image.convert("L")
    pixels = grayscale_image.getdata()

    # Generate ASCII art from pixel data
    ascii_frame = ""
    for j, pixel in enumerate(pixels):
        if j % new_width == 0 and j != 0:
            ascii_frame += "\n"
        ascii_frame += ascii_chars[pixel // 25]
    
    # Save ASCII art as a text file
    output_path = os.path.join(output_dir, f"frame{i:03}.txt")
    with open(output_path, "w") as file:
        file.write(ascii_frame)
