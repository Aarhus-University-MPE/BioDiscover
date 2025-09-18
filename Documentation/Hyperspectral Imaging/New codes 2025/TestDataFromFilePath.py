from pathlib import Path

# === User input: just paste the full file path here ===
full_path_str = r"C:/Projects/BioDiscover/Documentation/Hyperspectral Imaging/External files/Billeder 2023/Billede pakker/Originals/2022-10-5_12-49-42_1296x1000x900_imageCube.bin"

# Convert to Path object (handles slashes & filenames safely)
full_path = Path(full_path_str)

# Extract components
folder = full_path.parent           # folder path (as Path)
filename_with_ext = full_path.name  # 'image_1.npy'
FileName = full_path.stem           # 'image_1' (without extension)
extension = full_path.suffix        # '.npy'

# Attempt to extract date and time from the filename, if available
# E.g., '2022-10-5_12-49-42_1296x1000x900_imageCube'
# We'll try to extract parts from the string if it matches a known format
import re

match = re.match(r"(\d{4}-\d{1,2}-\d{1,2})_(\d{2}-\d{2}-\d{2})", FileName)
if match:
    date_raw = match.group(1)  # '2022-10-5'
    time = match.group(2)      # '12-49-42'
    # Convert to YYMMDD format for consistency
    parts = date_raw.split('-')
    date = parts[0][2:] + parts[1].zfill(2) + parts[2].zfill(2)  # → '221005'
else:
    date = "unknown"
    time = "unknown"

# Output for verification
print("📁 Folder: ", folder)
print("📄 Filename: ", FileName)
print("📂 Extension: ", extension)
print("📆 Date: ", date)
print("⏰ Time: ", time)
