# This file was created by Jeppe Fogh Rasmussen
# This script converts a binary file (.bin) containing hyperspectral imaging data into a NumPy array (.npy).
# The binary file is expected to have a specific shape and format.
# The script checks the file size, reads the data, reshapes it into a 3D array, and saves it as a .npy file.

import numpy as np
import os

# === USER Input ===
path = "C:/Projects/BioDiscover/Documentation/Hyperspectral Imaging/External files/Billeder 2023/Billede pakker/Originals/"
filename = '2022-10-5_12-59-26_1296x1000x900_imageCube'
bin_file = os.path.join(path, filename + '.bin')
npy_path = "C:/Projects/BioDiscover/Documentation/Hyperspectral Imaging/External files/Billeder 2023/Billede pakker/"

# === KNOWN SHAPE AND FORMAT ===
width = 1296    # Across conveyor belt
height = 1000   # Number of scanned lines
channels = 900  # Number of spectral channels
dtype = np.uint8

# === LOAD THE .bin FILE ===
expected_size = width * height * channels  # 1,166,400,000 bytes
actual_size = os.path.getsize(bin_file)

if expected_size != actual_size:
    raise ValueError(f"File size mismatch! Expected {expected_size} bytes, got {actual_size} bytes.")

print("Loading binary data...")
data = np.fromfile(bin_file, dtype=dtype)

# === RESHAPE TO 3D ARRAY ===
print("Reshaping data into (channels, height, width)...")
datacube = data.reshape((channels, height, width))

# === SAVE TO .npy UNDER A NEW NAME ===
npy_filename = filename + '_converted.npy'
npy_file = os.path.join(npy_path, npy_filename)

print(f"Saving to {npy_file} ...")
np.save(npy_file, datacube)

print("Conversion complete. Original .bin file untouched.")