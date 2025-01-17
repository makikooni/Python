from PIL import Image
import numpy as np
import os

# Load the image
image_path = '/Users/wefalinska/Github/Python/veggie.png'  # Replace with your image path
image = Image.open(image_path).convert("RGBA")
image_data = np.array(image)

# Extract the alpha channel
alpha_channel = image_data[:, :, 3]

# Find non-transparent pixels
non_transparent_indices = np.argwhere(alpha_channel > 0)

# Sort non-transparent pixels by vertical position (y-axis)
sorted_indices = non_transparent_indices[np.argsort(non_transparent_indices[:, 0])]

# Define split ratios
ratios = [40, 30, 30, 5, 5]
total_ratio = sum(ratios)

# Calculate the number of pixels for each split
total_visible_pixels = len(sorted_indices)
split_counts = [int(total_visible_pixels * (r / total_ratio)) for r in ratios]

# Adjust the last split to cover any remaining pixels
split_counts[-1] += total_visible_pixels - sum(split_counts)

# Create output directory
output_dir = "apple_splits_shape_awares"
os.makedirs(output_dir, exist_ok=True)

# Generate masks and save each split
start_idx = 0
for i, count in enumerate(split_counts):
    end_idx = start_idx + count
    split_mask = np.zeros_like(alpha_channel)
    split_pixels = sorted_indices[start_idx:end_idx]
    for y, x in split_pixels:
        split_mask[y, x] = 255
    
    # Apply mask to the original image
    split_image_data = image_data.copy()
    split_image_data[:, :, 3] = split_mask
    split_image = Image.fromarray(split_image_data, mode="RGBA")
    split_image.save(f"{output_dir}/apple_part_{i+1}.png")
    
    start_idx = end_idx

print("Shape-aware splitting complete. Images saved in:", output_dir)
