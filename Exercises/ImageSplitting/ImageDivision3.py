import numpy as np
import random
from PIL import Image
import os

# Load the image
image_path = 'veggie2.png'  # Replace with your image path
image = Image.open(image_path).convert("RGBA")
image_data = np.array(image)

# Extract the alpha channel (transparency)
alpha_channel = image_data[:, :, 3]

# Find non-transparent pixels
non_transparent_indices = np.argwhere(alpha_channel > 0)
total_visible_pixels = len(non_transparent_indices)

# Shuffle the non-transparent pixels randomly
random.shuffle(non_transparent_indices.tolist())

# Define split ratios
ratios = [40, 20, 20, 15, 5]
total_ratio = sum(ratios)

# Calculate the number of pixels for each split
split_counts = [int(total_visible_pixels * (r / total_ratio)) for r in ratios]

# Ensure all pixels are accounted for
split_counts[-1] += total_visible_pixels - sum(split_counts)

# Create output directory
output_dir = "veggie_pixel_random_touch"
os.makedirs(output_dir, exist_ok=True)

# Function to get neighbors (8-connected, diagonal included)
def get_neighbors(pixel, width, height):
    y, x = pixel  # Note: y, x order
    neighbors = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ny, nx = y + dy, x + dx
            if 0 <= nx < width and 0 <= ny < height:
                neighbors.append((ny, nx))
    return neighbors

# Function to grow a connected region from a seed pixel
def grow_blob(seed_pixel, width, height, max_size, selected_pixels):
    blob = set()
    blob.add(seed_pixel)
    to_explore = [seed_pixel]
    
    while to_explore and len(blob) < max_size:
        current_pixel = to_explore.pop()
        neighbors = get_neighbors(current_pixel, width, height)
        random.shuffle(neighbors)
        
        for neighbor in neighbors:
            ny, nx = neighbor  # Note: y, x order
            if neighbor not in blob and neighbor not in selected_pixels and alpha_channel[ny, nx] > 0:
                blob.add(neighbor)
                to_explore.append(neighbor)
                if len(blob) >= max_size:
                    break
    return list(blob)

# Generate masks and save each random group
selected_pixels = set()
all_pixels_covered = set(tuple(p) for p in non_transparent_indices)

for i, count in enumerate(split_counts):
    blob_pixels = []
    
    while len(blob_pixels) < count:
        # Randomly pick a seed pixel
        remaining_pixels = list(all_pixels_covered - selected_pixels)
        if not remaining_pixels:
            break
        
        seed_pixel = random.choice(remaining_pixels)
        
        # Grow a blob from this seed
        blob = grow_blob(seed_pixel, image_data.shape[1], image_data.shape[0], count - len(blob_pixels), selected_pixels)
        blob_pixels.extend(blob)
        selected_pixels.update(blob)
    
    # Create a mask for the selected pixels
    split_mask = np.zeros_like(alpha_channel)
    for y, x in blob_pixels:  # Note: y, x order
        split_mask[y, x] = 255
    
    # Apply mask to the original image
    split_image_data = image_data.copy()
    split_image_data[:, :, 3] = split_mask
    split_image = Image.fromarray(split_image_data, mode="RGBA")
    split_image.save(f"{output_dir}/veggie_pixel_random_touch{i+1}.png")
    
    print(f"Saved image group {i+1} with {len(blob_pixels)} pixels.")

# Final check to ensure all pixels are covered
assert len(selected_pixels) == total_visible_pixels, "Not all pixels are accounted for!"
print("All pixels are covered and images saved successfully.")
