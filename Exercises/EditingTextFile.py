import re

# Open the original file with UTF-8 encoding
with open("words.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Step 1: Remove leading numbers and spaces using regex
lines = [re.sub(r"^\d+\s+", "", line.strip()) for line in lines]

# Step 2: Keep only the first character of each cleaned line
edited_lines = [line[0] + "\n" if line else "\n" for line in lines]

# Save the processed lines to a new file
with open("processed_file.txt", "w", encoding="utf-8") as file:
    file.writelines(edited_lines)

print("Processing complete! Check 'processed_file.txt'.")
