# Importing packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from datetime import datetime
from fileinput import filename
from gettext import Catalog
from operator import truediv
from matplotlib.patches import Rectangle
from pathlib import Path
import re

# ----------------------------------------------
# USER INPUT AND BASIC SETUP
# ----------------------------------------------

# full_path_str = r"C:\...\imageCube.bin"
full_path_str = r"C:\Projects\BioDiscover\Documentation\Hyperspectral Imaging\External files\Billeder 2024\image_1.npy"

full_path = Path(full_path_str)
folder = full_path.parent
filename_with_ext = full_path.name
FileName = full_path.stem
extension = full_path.suffix
filepath = Path(full_path)

# Try extracting date & time from filename
match = re.match(r"(\d{4}-\d{1,2}-\d{1,2})_(\d{2}-\d{2}-\d{2})", FileName)
if match:
    date_raw = match.group(1)
    time = match.group(2)
    parts = date_raw.split('-')
    date = parts[0][2:] + parts[1].zfill(2) + parts[2].zfill(2)
else:
    date = "unknown"
    time = "unknown"

print("📁 Folder: ", folder)
print("📄 Filename: ", FileName)
print("📂 Extension: ", extension)
print("📆 Date: ", date)
print("⏰ Time: ", time)

# Create calibration subfolder
if date == "unknown" or time == "unknown":
    Calibration_folder = FileName
else:
    Calibration_folder = date + "_" + time

now = datetime.now()
current_date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
output_folder = os.path.join(folder, Calibration_folder, f"Calibration-Date_{current_date_time}")
output_path = os.path.join(output_folder + "/")
os.makedirs(output_folder, exist_ok=True)
print(f"Calibration results will be saved to: {output_folder}")

verbose = True

# ----------------------------------------------
# LOAD HYPERSPECTRAL FILE (.bin or .npy)
# ----------------------------------------------
x = 900     # height
y = 1392    # width
wave = 1044 # spectral channels
expected_shape = (wave, x, y)

if extension == '.npy':
    datacube = np.load(filepath)

    if not isinstance(datacube, np.ndarray):
        raise ValueError("Loaded .npy file is not a NumPy array.")
    if datacube.ndim != 3:
        raise ValueError(f"Expected 3D array, got shape: {datacube.shape}")

    if verbose:
        print(f"Detected raw shape: {datacube.shape}")

    shape = datacube.shape
    dim_map = {}
    for i, dim in enumerate(shape):
        if dim == wave:
            dim_map['C'] = i
        elif dim == x:
            dim_map['H'] = i
        elif dim == y:
            dim_map['W'] = i
        else:
            raise ValueError(f"Unexpected dimension size {dim} in .npy file.")

    if set(dim_map.keys()) != {'C', 'H', 'W'}:
        raise ValueError(f"Could not detect all required dimensions from shape: {shape}")

    # Transpose to (H, W, C)
    transpose_order = [dim_map['H'], dim_map['W'], dim_map['C']]
    datacube = np.transpose(datacube, transpose_order)

    if verbose:
        print(f"✅ .npy final loaded shape: {datacube.shape} (H, W, C)")

    # Save rotated copy
    rotated_filename = f"rotated_{FileName}.npy"
    rotated_path = Path(output_folder) / rotated_filename
    np.save(rotated_path, datacube)
    print(f"✅ Saved rotated cube: {rotated_path}")

elif extension == '.bin':
    # Existing .bin reading logic (unchanged)
    datacube = np.fromfile(filepath, dtype=np.float32).reshape(expected_shape)
    datacube = np.transpose(datacube, (1, 2, 0))  # (H, W, C)

# ----------------------------------------
# SPATIAL X CALIBRATION
# ----------------------------------------
X_peaks = []
for j in range(0, 8):
    X_area = datacube[X_spat_x1:X_spat_x2,
                      X_spat_y1 + distance * j:X_spat_y2 + distance * j,
                      :]

    # Same axis for both .npy and .bin
    X_mean_area = np.mean(X_area, axis=1)  # mean across W
    X_mean_area = np.mean(X_mean_area, axis=1)  # mean over channels

    threshold_X = np.mean(X_mean_area, axis=0)
    for i in range(len(X_mean_area) - 1):
        if X_mean_area[i] > threshold_X and X_mean_area[i + 1] < threshold_X:
            X_peaks.append(i)
        elif X_mean_area[i] < threshold_X and X_mean_area[i + 1] > threshold_X:
            X_peaks.append(i)

X_lengths_pixels = np.diff(X_peaks)
selected_indices = np.where(X_min < X_lengths_pixels)[0]
X_lengths_pixels = X_lengths_pixels[selected_indices]
X_length_pixels = np.mean(X_lengths_pixels)
X_coeff = 15.0 / X_length_pixels

# ----------------------------------------
# SPATIAL Y CALIBRATION
# ----------------------------------------
Y_peaks = []
for _ in range(0, 2):
    Y_area = datacube[Y_spat_x1 + distance2 * _:Y_spat_x2 + distance2 * _,
                      Y_spat_y1:Y_spat_y2,
                      :]

    # Same axis for both .npy and .bin
    Y_mean_area = np.mean(Y_area, axis=0)  # mean across H
    Y_mean_area = np.mean(Y_mean_area, axis=1)  # mean over channels

    threshold_Y = np.mean(Y_mean_area, axis=0)
    for i in range(len(Y_mean_area) - 1):
        if Y_mean_area[i] > threshold_Y and Y_mean_area[i + 1] < threshold_Y:
            Y_peaks.append(i)
        elif Y_mean_area[i] < threshold_Y and Y_mean_area[i + 1] > threshold_Y:
            Y_peaks.append(i)

Y_lengths_pixels = np.diff(Y_peaks)
selected_indices = np.where(Y_min < Y_lengths_pixels)[0]
Y_lengths_pixels = Y_lengths_pixels[selected_indices]
Y_length_pixels = np.mean(Y_lengths_pixels)
Y_coeff = 15.0 / Y_length_pixels

# ----------------------------------------
# FINAL COEFFICIENTS
# ----------------------------------------
spat_coeff = np.reshape(np.array([X_coeff, Y_coeff]), (1, 2))
if 'final_coefficients' not in locals() or final_coefficients is None:
    final_coefficients = spat_coeff
else:
    final_coefficients = np.append(final_coefficients, spat_coeff, axis=0)

# ----------------------------------------
# PLOT SPATIAL CALIBRATION (OPTIONAL)
# ----------------------------------------
if SanitySpatial:
    plt.figure()
    plt.plot(range(len(X_lengths_pixels)), X_lengths_pixels, 'kX')
    plt.xlabel("Square number")
    plt.ylabel("Square width in pixels")
    plt.title("Comparison of square widths in X")
    plt.show()

    plt.figure()
    plt.plot(range(len(Y_lengths_pixels)), Y_lengths_pixels, 'kX')
    plt.xlabel("Square number")
    plt.ylabel("Square width [pixels]")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.yticks(np.arange(min(Y_lengths_pixels),
                         max(Y_lengths_pixels) + 1, 1.0))
    plt.title("Comparison of square widths in Y")
    plt.show()
