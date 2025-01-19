from PIL import Image
import numpy as np
import os
import random

# Load the image
image_path = 'veggie2.png'  # Replace with your image path
image = Image.open(image_path).convert("RGBA")
image_data = np.array(image)

# Extract the alpha channel (transparency)
alpha_channel = image_data[:, :, 3]

# Find non-transparent pixels (where alpha > 0)
non_transparent_indices = np.argwhere(alpha_channel > 0)

# Shuffle the non-transparent pixels randomly (once, to prevent overlap)
non_transparent_indices = non_transparent_indices.tolist()
random.shuffle(non_transparent_indices)

# Define split ratios (e.g., 40%, 20%, 20%, 15%, 5%)
ratios = [40, 20, 20, 15, 5]
total_ratio = sum(ratios)

# Calculate how many pixels go into each chunk
total_visible_pixels = len(non_transparent_indices)
split_counts = [int(total_visible_pixels * (r / total_ratio)) for r in ratios]

# Adjust the last split to ensure all pixels are used
split_counts[-1] += total_visible_pixels - sum(split_counts)

# Create output directory
output_dir = "veggie2_pixel_random_fixed"
os.makedirs(output_dir, exist_ok=True)

# Split and save the image chunks
start_idx = 0
for i, count in enumerate(split_counts):
    end_idx = start_idx + count

    # Select unique pixels for this chunk (no overlaps)
    chunk_pixels = non_transparent_indices[start_idx:end_idx]

    # Create a blank mask for this chunk
    chunk_mask = np.zeros_like(alpha_channel)

    # Apply the selected pixels to the mask
    for y, x in chunk_pixels:
        chunk_mask[y, x] = 255

    # Apply the mask to the original image data
    chunk_image_data = image_data.copy()
    chunk_image_data[:, :, 3] = chunk_mask

    # Convert to image and save
    chunk_image = Image.fromarray(chunk_image_data, mode="RGBA")
    chunk_image.save(f"{output_dir}/veggie_pixel_random_fixed_{i+1}.png")

    start_idx = end_idx  # Move to the next chunk

print("Random chunk splitting complete. No missing pixels!")
