import numpy as np
import os

# === USER SETTINGS ===
path = "C:/Projects/Hyperspectral analysis/13 Hyperspektralt/Fra Bachelor/Billede pakker/"
filename = '2022-10-5_12-57-43_1296x1000x900_imageCube'
bin_file = os.path.join(path, filename + '.bin')

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
npy_file = os.path.join(path, npy_filename)

print(f"Saving to {npy_file} ...")
np.save(npy_file, datacube)

print("Conversion complete. Original .bin file untouched.")