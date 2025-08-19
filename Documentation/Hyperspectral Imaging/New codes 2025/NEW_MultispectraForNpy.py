# This script is used to visualize the hyperspectral data.
# It extracts the average spectrum from specified coordinates in the hyperspectral datacube.
# It also calculates the ratio of integrated values in specified wavelength ranges.
# The script is customizable for different datasets and regions of interest.

'''
How to use this script:
1. Set the `path` variable to the directory where your hyperspectral data files are located
2. Change the `filename` variable to the name of the data file you want to analyze
3. Adjust the `chanal` variable to specify the channel you want to visualize
4. Modify the Coordinate variables (e.g., `XE3`, `YE3`, etc.) to match the specific regions of interest in your data
5. Uncomment the sections of code corresponding to the dishes you want to analyze by removing the `#` at the beginning
6. Run the script to see the results printed in the console
'''

##########################################
# Importing python packages
##########################################
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from matplotlib.patches import Rectangle
from pathlib import Path

##########################################
# USER INPUT AND BASIC SETUP
##########################################

# === User input: just paste the full file path here ===
# full_path_str = r"C:\Projects\BioDiscover\Documentation\Hyperspectral Imaging\External files\Billeder 2023\Billede pakker\Originals\2022-10-5_12-49-42_1296x1000x900_imageCube.bin"
full_path_str = r"C:\Projects\BioDiscover\Documentation\Hyperspectral Imaging\External files\Billeder 2024\image_1.npy"

chanal = 630        # channel to visualize

# Convert to Path object (handles slashes & filenames safely)
full_path = Path(full_path_str) 

# Extract components
folder = full_path.parent           # folder path (as Path)
filename_with_ext = full_path.name  # 'image_1.npy'
FileName = full_path.stem           # 'image_1' (without extension)
extension = full_path.suffix        # '.npy'
filepath = Path(full_path)

# Attempt to extract date and time from the filename, if available
# E.g., '2022-10-5_12-49-42_1296x1000x900_imageCube'
# We'll try to extract parts from the string if it matches a known format

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

print(f"Loading: {FileName + extension}")



verbose = True  # When TRUE: Prints additional information during processing

##########################################
# Coordinates for objects in dishes
##########################################

'''Excample Coordinates for dish j
XAj = [254,465,450,403,461,465,494,525,553,605,576,644,585,597,685,699,728,729,863] #Arthropod coordinates
YAj = [286, 38, 52,247,268,281,260,241,205,273,355,267,134,157,194,140,101,135,176]
XBj = [190,522] #Belt coordinates
YBj = [66, 626]
XDj = [650, 683, 743, 783] #Dirt coordinates
YDj = [275, 297, 272, 256]
XEj = [430, 518] #Ethanol coordinates
YEj = [117, 92]
XPj = [576, 582, 620] #Plant coordinates
YPj = [117, 150, 160]
XSj = [361, 381, 497] #Stone and rock coordinates
YSj = [179, 244, 228]
XUj = [623, 701, 680, 788] #objects that are not clear to identify or unidentified by design
YUj = [74, 114, 163, 143]
'''

'''Coordinates for dish 0'''
XA0 = [] #Arthropod coordinates
YA0 = []
XB0 = [] #Belt coordinates
YB0 = []
XD0 = [] #Dirt coordinates
YD0 = []
XE0 = [] #Ethanol coordinates
YE0 = []
XP0 = [] #Plant coordinates
YP0 = []
XS0 = [] #Stone and rock coordinates
YS0 = []
XU0 = [] #objects that are not clear to identify or unidentified by design
YU0 = []

'''Coordinates for dish 1'''
XA1 = [] #Arthropod coordinates
YA1 = []
XB1 = [] #Belt coordinates
YB1 = []
XD1 = [] #Dirt coordinates
YD1 = []
XE1 = [] #Ethanol coordinates
YE1 = []
XP1 = [] #Plant coordinates
YP1 = []
XS1 = [] #Stone and rock coordinates
YS1 = []
XU1 = [] #objects that are not clear to identify or unidentified by design
YU1 = []

'''Coordinates for dish 2'''
XA2 = [] #Arthropod coordinates
YA2 = []
XB2 = [] #Belt coordinates
YB2 = []
XD2 = [] #Dirt coordinates
YD2 = []
XE2 = [] #Ethanol coordinates
YE2 = []
XP2 = [] #Plant coordinates
YP2 = []
XS2 = [] #Stone and rock coordinates
YS2 = []
XU2 = [] #objects that are not clear to identify or unidentified by design
YU2 = []

'''Coordinates for dish 3'''
XA3 = [] #Arthropod coordinates
YA3 = []
XB3 = [] #Belt coordinates
YB3 = []
XD3 = [] #Dirt coordinates
YD3 = []
XE3 = [] #Ethanol coordinates
YE3 = []
XP3 = [] #Plant coordinates
YP3 = []
XS3 = [] #Stone and rock coordinates
YS3 = []
XU3 = [] #objects that are not clear to identify or unidentified by design
YU3 = []

'''Coordinates for dish 4'''
XA4 = [] #Arthropod coordinates
YA4 = []
XB4 = [] #Belt coordinates
YB4 = []
XD4 = [] #Dirt coordinates
YD4 = []
XE4 = [] #Ethanol coordinates
YE4 = []
XP4 = [] #Plant coordinates
YP4 = []
XS4 = [] #Stone and rock coordinates
YS4 = []
XU4 = [] #objects that are not clear to identify or unidentified by design
YU4 = []

'''Coordinates for dish 5'''
XA5 = [] #Arthropod coordinates
YA5 = []
XB5 = [] #Belt coordinates
YB5 = []
XD5 = [] #Dirt coordinates
YD5 = []
XE5 = [] #Ethanol coordinates
YE5 = []
XP5 = [] #Plant coordinates
YP5 = []
XS5 = [] #Stone and rock coordinates
YS5 = []
XU5 = [] #objects that are not clear to identify or unidentified by design
YU5 = []

'''Coordinates for dish 6'''
XA6 = [] #Arthropod coordinates
YA6 = []
XB6 = [] #Belt coordinates
YB6 = []
XD6 = [] #Dirt coordinates
YD6 = []
XE6 = [] #Ethanol coordinates
YE6 = []
XP6 = [] #Plant coordinates
YP6 = []
XS6 = [] #Stone and rock coordinates
YS6 = []
XU6 = [] #objects that are not clear to identify or unidentified by design
YU6 = []

'''Coordinates for dish 7'''
XA7 = [] #Arthropod coordinates
YA7 = []
XB7 = [] #Belt coordinates
YB7 = []
XD7 = [] #Dirt coordinates
YD7 = []
XE7 = [] #Ethanol coordinates
YE7 = []
XP7 = [] #Plant coordinates
YP7 = []
XS7 = [] #Stone and rock coordinates
YS7 = []
XU7 = [] #objects that are not clear to identify or unidentified by design
YU7 = []

'''Coordinates for dish 8'''
XA8 = [] #Arthropod coordinates
YA8 = []
XB8 = [] #Belt coordinates
YB8 = []
XD8 = [] #Dirt coordinates
YD8 = []
XE8 = [] #Ethanol coordinates
YE8 = []
XP8 = [] #Plant coordinates
YP8 = []
XS8 = [] #Stone and rock coordinates
YS8 = []
XU8 = [] #objects that are not clear to identify or unidentified by design
YU8 = []

'''Coordinates for dish 9'''
XA9 = [] #Arthropod coordinates
YA9 = []
XB9 = [] #Belt coordinates
YB9 = []
XD9 = [] #Dirt coordinates
YD9 = []
XE9 = [] #Ethanol coordinates
YE9 = []
XP9 = [] #Plant coordinates
YP9 = []
XS9 = [] #Stone and rock coordinates
YS9 = []
XU9 = [] #objects that are not clear to identify or unidentified by design
YU9 = []


####################################################################################
# Plotting the average spectrum of the pixels in the selection
####################################################################################
def get_spectrum(x1,x2,y1,y2): 
    spectrum = datacube[:,y1:y2,x1:x2]
    spectrum = np.mean(spectrum,axis=1)
    spectrum = np.mean(spectrum,axis=1)
    return spectrum


datacube = np.load(filepath)

if not isinstance(datacube, np.ndarray):
    raise ValueError("Loaded .npy file is not a NumPy array.")

if datacube.ndim != 3:
    raise ValueError(f"Expected 3D array, got shape: {datacube.shape}")

if verbose:
    print(f"Detected raw shape: {datacube.shape}")

shape = datacube.shape

if verbose:        
    print(f"✅ Final shape after rotation: {datacube.shape} (H, W, C)")

####################################################################################
# Data cupe size (These values can be obtaind from the file size or name)
####################################################################################
x = 900                 # H-height (number of lines)
y = 1392                 # W-width across belt
wave = 1044               # C-number of spectral channels
expected_shape = (x, y, wave)

# Final shape check
if expected_shape:
    if datacube.shape != expected_shape:
        print(f"⚠️ Warning: Image shape {datacube.shape} does not match expected {expected_shape}")
    else:
        if verbose:
            print("✅ Shape matches expected.")

# Figure shoving an image of the datacube
fig, ax = plt.subplots(figsize=(14, 6))  # (width_inches, height_inches)

datacube = np.transpose(datacube, (1, 0, 2))  #transpose to (H, W, C) -> (W, H, C) for visuals

ax.imshow(datacube[:, :, chanal], cmap='Greys_r', origin="lower", aspect=0.25)
plt.title(f'Dish {FileName} | Channel {chanal}') #Add name to plot

ax.set_xlabel('Along conveyer belt')
ax.set_ylabel('Across conveyer belt')

plt.show() #Shows the image

##########################################
#Wavelength calibration 
##########################################
A = 1.16065 #Calibration factor
B = 315.03 #Calibration offset
axis_l = np.arange(1044)*A+B      #creating band-wavelength table
delta=5

####################################################################################
# Dish selection (Case structure)
####################################################################################
FileNumber = int(FileName.split('_')[1])  # Extracting the dish number from the filename
print(f"Selected Dish: {FileNumber}")

''' Example case: j
        for i in range(len(XAj)): # Arthropod coordinates
            A_data=get_spectrum(XAj[i],XAj[i]+delta,YAj[i],YAj[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XBj)): # Belt coordinates
            A_data=get_spectrum(XBj[i],XBj[i]+delta,YBj[i],YBj[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XDj)): # Dirt coordinates
            A_data=get_spectrum(XDj[i],XDj[i]+delta,YDj[i],YDj[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XEj)): # Ethanol coordinates
            A_data=get_spectrum(XEj[i],XEj[i]+delta,YEj[i],YEj[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XPj)):
            A_data=get_spectrum(XPj[i],XPj[i]+delta,YPj[i],YPj[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XSj)):
            A_data=get_spectrum(XSj[i],XSj[i]+delta,YSj[i],YSj[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XUj)):
            A_data=get_spectrum(XUj[i],XUj[i]+delta,YUj[i],YUj[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 
    '''

match FileNumber:
   
    case 0:
        for i in range(len(XA0)): # Arthropod coordinates
            A_data=get_spectrum(XA0[i],XA0[i]+delta,YA0[i],YA0[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB0)): # Belt coordinates
            A_data=get_spectrum(XB0[i],XB0[i]+delta,YB0[i],YB0[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD0)): # Dirt coordinates
            A_data=get_spectrum(XD0[i],XD0[i]+delta,YD0[i],YD0[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE0)): # Ethanol coordinates
            A_data=get_spectrum(XE0[i],XE0[i]+delta,YE0[i],YE0[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP0)):
            A_data=get_spectrum(XP0[i],XP0[i]+delta,YP0[i],YP0[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS0)):
            A_data=get_spectrum(XS0[i],XS0[i]+delta,YS0[i],YS0[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU0)):
            A_data=get_spectrum(XU0[i],XU0[i]+delta,YU0[i],YU0[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 1:
        for i in range(len(XA1)): # Arthropod coordinates
            A_data=get_spectrum(XA1[i],XA1[i]+delta,YA1[i],YA1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB1)): # Belt coordinates
            A_data=get_spectrum(XB1[i],XB1[i]+delta,YB1[i],YB1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD1)): # Dirt coordinates
            A_data=get_spectrum(XD1[i],XD1[i]+delta,YD1[i],YD1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE1)): # Ethanol coordinates
            A_data=get_spectrum(XE1[i],XE1[i]+delta,YE1[i],YE1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP1)):
            A_data=get_spectrum(XP1[i],XP1[i]+delta,YP1[i],YP1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS1)):
            A_data=get_spectrum(XS1[i],XS1[i]+delta,YS1[i],YS1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU1)):
            A_data=get_spectrum(XU1[i],XU1[i]+delta,YU1[i],YU1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 2:
        for i in range(len(XA2)): # Arthropod coordinates
            A_data=get_spectrum(XA2[i],XA2[i]+delta,YA2[i],YA2[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB2)): # Belt coordinates
            A_data=get_spectrum(XB2[i],XB2[i]+delta,YB2[i],YB2[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD2)): # Dirt coordinates
            A_data=get_spectrum(XD2[i],XD2[i]+delta,YD2[i],YD2[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE2)): # Ethanol coordinates
            A_data=get_spectrum(XE2[i],XE2[i]+delta,YE2[i],YE2[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP2)):
            A_data=get_spectrum(XP2[i],XP2[i]+delta,YP2[i],YP2[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS2)):
            A_data=get_spectrum(XS2[i],XS2[i]+delta,YS2[i],YS2[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU2)):
            A_data=get_spectrum(XU2[i],XU2[i]+delta,YU2[i],YU2[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 3:
        for i in range(len(XA3)): # Arthropod coordinates
            A_data=get_spectrum(XA3[i],XA3[i]+delta,YA3[i],YA3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB3)): # Belt coordinates
            A_data=get_spectrum(XB3[i],XB3[i]+delta,YB3[i],YB3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD3)): # Dirt coordinates
            A_data=get_spectrum(XD3[i],XD3[i]+delta,YD3[i],YD3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE3)): # Ethanol coordinates
            A_data=get_spectrum(XE3[i],XE3[i]+delta,YE3[i],YE3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP3)):
            A_data=get_spectrum(XP3[i],XP3[i]+delta,YP3[i],YP3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS3)):
            A_data=get_spectrum(XS3[i],XS3[i]+delta,YS3[i],YS3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU3)):
            A_data=get_spectrum(XU3[i],XU3[i]+delta,YU3[i],YU3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 4:
        for i in range(len(XA4)): # Arthropod coordinates
            A_data=get_spectrum(XA4[i],XA4[i]+delta,YA4[i],YA4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB4)): # Belt coordinates
            A_data=get_spectrum(XB4[i],XB4[i]+delta,YB4[i],YB4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD4)): # Dirt coordinates
            A_data=get_spectrum(XD4[i],XD4[i]+delta,YD4[i],YD4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE4)): # Ethanol coordinates
            A_data=get_spectrum(XE4[i],XE4[i]+delta,YE4[i],YE4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP4)):
            A_data=get_spectrum(XP4[i],XP4[i]+delta,YP4[i],YP4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS4)):
            A_data=get_spectrum(XS4[i],XS4[i]+delta,YS4[i],YS4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU4)):
            A_data=get_spectrum(XU4[i],XU4[i]+delta,YU4[i],YU4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 5:
        for i in range(len(XA5)): # Arthropod coordinates
            A_data=get_spectrum(XA5[i],XA5[i]+delta,YA5[i],YA5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB5)): # Belt coordinates
            A_data=get_spectrum(XB5[i],XB5[i]+delta,YB5[i],YB5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD5)): # Dirt coordinates
            A_data=get_spectrum(XD5[i],XD5[i]+delta,YD5[i],YD5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE5)): # Ethanol coordinates
            A_data=get_spectrum(XE5[i],XE5[i]+delta,YE5[i],YE5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP5)):
            A_data=get_spectrum(XP5[i],XP5[i]+delta,YP5[i],YP5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS5)):
            A_data=get_spectrum(XS5[i],XS5[i]+delta,YS5[i],YS5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU5)):
            A_data=get_spectrum(XU5[i],XU5[i]+delta,YU5[i],YU5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 6:
        for i in range(len(XA6)): # Arthropod coordinates
            A_data=get_spectrum(XA6[i],XA6[i]+delta,YA6[i],YA6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB6)): # Belt coordinates
            A_data=get_spectrum(XB6[i],XB6[i]+delta,YB6[i],YB6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD6)): # Dirt coordinates
            A_data=get_spectrum(XD6[i],XD6[i]+delta,YD6[i],YD6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE6)): # Ethanol coordinates
            A_data=get_spectrum(XE6[i],XE6[i]+delta,YE6[i],YE6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP6)):
            A_data=get_spectrum(XP6[i],XP6[i]+delta,YP6[i],YP6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS6)):
            A_data=get_spectrum(XS6[i],XS6[i]+delta,YS6[i],YS6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU6)):
            A_data=get_spectrum(XU6[i],XU6[i]+delta,YU6[i],YU6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 7:
        for i in range(len(XA7)): # Arthropod coordinates
            A_data=get_spectrum(XA7[i],XA7[i]+delta,YA7[i],YA7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB7)): # Belt coordinates
            A_data=get_spectrum(XB7[i],XB7[i]+delta,YB7[i],YB7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD7)): # Dirt coordinates
            A_data=get_spectrum(XD7[i],XD7[i]+delta,YD7[i],YD7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE7)): # Ethanol coordinates
            A_data=get_spectrum(XE7[i],XE7[i]+delta,YE7[i],YE7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP7)):
            A_data=get_spectrum(XP7[i],XP7[i]+delta,YP7[i],YP7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS7)):
            A_data=get_spectrum(XS7[i],XS7[i]+delta,YS7[i],YS7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU7)):
            A_data=get_spectrum(XU7[i],XU7[i]+delta,YU7[i],YU7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 

    case 8:
        for i in range(len(XA8)): # Arthropod coordinates
            A_data=get_spectrum(XA8[i],XA8[i]+delta,YA8[i],YA8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB8)): # Belt coordinates
            A_data=get_spectrum(XB8[i],XB8[i]+delta,YB8[i],YB8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD8)): # Dirt coordinates
            A_data=get_spectrum(XD8[i],XD8[i]+delta,YD8[i],YD8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE8)): # Ethanol coordinates
            A_data=get_spectrum(XE8[i],XE8[i]+delta,YE8[i],YE8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP8)):
            A_data=get_spectrum(XP8[i],XP8[i]+delta,YP8[i],YP8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS8)):
            A_data=get_spectrum(XS8[i],XS8[i]+delta,YS8[i],YS8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU8)):
            A_data=get_spectrum(XU8[i],XU8[i]+delta,YU8[i],YU8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 
    case 9:
        for i in range(len(XA9)): # Arthropod coordinates
            A_data=get_spectrum(XA9[i],XA9[i]+delta,YA9[i],YA9[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r') 
        for i in range(len(XB9)): # Belt coordinates
            A_data=get_spectrum(XB9[i],XB9[i]+delta,YB9[i],YB9[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XD9)): # Dirt coordinates
            A_data=get_spectrum(XD9[i],XD9[i]+delta,YD9[i],YD9[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g') 
        for i in range(len(XE9)): # Ethanol coordinates
            A_data=get_spectrum(XE9[i],XE9[i]+delta,YE9[i],YE9[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')
        for i in range(len(XP9)):
            A_data=get_spectrum(XP9[i],XP9[i]+delta,YP9[i],YP9[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'c') 
        for i in range(len(XS9)):
            A_data=get_spectrum(XS9[i],XS9[i]+delta,YS9[i],YS9[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'y') 
        for i in range(len(XU9)):
            A_data=get_spectrum(XU9[i],XU9[i]+delta,YU9[i],YU9[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'm') 


title = "Collected Spectrum of dish " + str(FileName)
plt.title(title, color = 'k')
plt.xlabel("Wavelength")
plt.ylabel("Intensity")

plt.show()  #Shows the average spectrum of the selected dish


''' Solo spectrum | If you need to find spectrographic signature of a specific thing | Make sure that the correct datafile is loaded
plt.figure()
fff = 1 # change per number; remember that 1=0
A_data=get_spectrum(XA4[fff],XA4[fff]+delta,YA4[fff],YA4[fff]+delta) #Change series as needed
A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
A_plot = plt.plot(axis_l,A_data, color = 'r')
plt.title("Spectrographic signature of " + "A" + str(fff+1) + " in dish 4", color = 'k') #This string is set specificly for dish 4, in these datasets
plt.xlabel("Wavelength")
plt.ylabel("Intensity")

plt.show() # Shows the spectrographic signature of a specific thing
#'''

'''Add barrier lines for visualisation of filter |If you want a visualisation of filter add a number-sign/hashtag
wave_1 = 980
wave_2 = wave_1 + 10
wave_3 = 1300
wave_4 = wave_3 + 10

plt.plot([wave_1,wave_1], [0,1], color = 'k')
plt.plot([wave_2,wave_2], [0,1], color = 'k')
plt.plot([wave_3,wave_3], [0,1], color = 'k')
plt.plot([wave_4,wave_4], [0,1], color = 'k')
plt.show() 
#'''