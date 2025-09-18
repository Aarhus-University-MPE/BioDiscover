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
full_path_str = r"C:\Projects\BioDiscover\Documentation\Hyperspectral Imaging\External files\Billeder 2024\image_4.npy"

chanal = 630  # channel to visualize

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

FileNumber = int(FileName.split('_')[1])  # Extracting the dish number from the filename
print(f"Selected Dish: {FileNumber}")

'''Excample Coordinates for dish j
XA = [254,465,450,403,461,465,494,525,553,605,576,644,585,597,685,699,728,729,863] #Arthropod coordinates
YA = [286, 38, 52,247,268,281,260,241,205,273,355,267,134,157,194,140,101,135,176]
XB = [190,522] #Belt coordinates
YB = [66, 626]
XD = [650, 683, 743, 783] #Dirt coordinates
YD = [275, 297, 272, 256]
XE = [430, 518] #Ethanol coordinates
YE = [117, 92]
XP = [576, 582, 620] #Plant coordinates
YP = [117, 150, 160]
XS = [361, 381, 497] #Stone and rock coordinates
YS = [179, 244, 228]
XU = [623, 701, 680, 788] #objects that are not clear to identify or unidentified by design
YU = [74, 114, 163, 143]
'''
match FileNumber:
    case 0: 
        '''Coordinates for dish 0'''
        XA = [727] #Arthropod coordinates
        YA = [645]
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [26, 35] #Plant coordinates
        YP = [703, 708]
        XS = [500] #Stone and rock coordinates
        YS = [500]
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 1:
        '''Coordinates for dish 1'''
        XA = [347, 359, 328, 339, 332, 346, 351] #Arthropod coordinates
        YA = [615, 658, 676, 685, 725, 737, 790]
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [492] #Plant coordinates
        YP = [782]
        XS = [500] #Stone and rock coordinates
        YS = [500]
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 2:
        '''Coordinates for dish 2'''
        XA = [] #Arthropod coordinates
        YA = []
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [] #Plant coordinates
        YP = []
        XS = [] #Stone and rock coordinates
        YS = []
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 3:
        '''Coordinates for dish 3'''
        XA = [] #Arthropod coordinates
        YA = []
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [] #Plant coordinates
        YP = []
        XS = [] #Stone and rock coordinates
        YS = []
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 4:
        '''Coordinates for dish 4'''
        XA = [57, 46, 63] #Arthropod coordinates
        YA = [613, 581, 576]
        XB = [] #Belt coordinates
        YB = []
        XD = [13] #Dirt coordinates
        YD = [648]
        XE = [] #Ethanol coordinates
        YE = []
        XP = [136] #Plant coordinates
        YP = [695]
        XS = [18] #Stone and rock coordinates
        YS = [735]
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 5:
        '''Coordinates for dish 5'''
        XA = [] #Arthropod coordinates
        YA = []
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [] #Plant coordinates
        YP = []
        XS = [] #Stone and rock coordinates
        YS = []
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 6:
        '''Coordinates for dish 6'''
        XA = [] #Arthropod coordinates
        YA = []
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [] #Plant coordinates
        YP = []
        XS = [] #Stone and rock coordinates
        YS = []
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 7:
        '''Coordinates for dish 7'''
        XA = [] #Arthropod coordinates
        YA = []
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [] #Plant coordinates
        YP = []
        XS = [] #Stone and rock coordinates
        YS = []
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 8:
        '''Coordinates for dish 8'''
        XA = [] #Arthropod coordinates
        YA = []
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [] #Plant coordinates
        YP = []
        XS = [] #Stone and rock coordinates
        YS = []
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []

    case 9:
        '''Coordinates for dish 9'''
        XA = [] #Arthropod coordinates
        YA = []
        XB = [] #Belt coordinates
        YB = []
        XD = [] #Dirt coordinates
        YD = []
        XE = [] #Ethanol coordinates
        YE = []
        XP = [] #Plant coordinates
        YP = []
        XS = [] #Stone and rock coordinates
        YS = []
        XU = [] #objects that are not clear to identify or unidentified by design
        YU = []


####################################################################################
# Plotting the average spectrum of the pixels in the selection
####################################################################################
''' def get_spectrum(x1,x2,y1,y2): 
    spectrum = datacube[y1:y2,x1:x2,:]
    spectrum = np.mean(spectrum,axis=2)
    spectrum = np.mean(spectrum,axis=2)
    return spectrum
    '''
    
def get_spectrum(x1, x2, y1, y2):
    # Slice: [height, width, channels]
    spectrum = datacube[y1:y2, x1:x2, :]      # shape: (Δy, Δx, C)
    spectrum = np.mean(spectrum, axis=(0, 1)) # average over spatial (y, x)
    return spectrum  # shape: (C,)

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
    
    
##########################################
#Wavelength calibration 
##########################################
A = 1.16065 #Calibration factor
B = 315.03 #Calibration offset
axis_l = np.arange(1044)*A+B      #creating band-wavelength table
delta=2
charlie = 10


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
plt.title(f'Dish {FileName} | Channel {chanal}') #Add name to plotD
ax.set_xlabel('Along conveyer belt')
ax.set_ylabel('Across conveyer belt')

for i in range(len(XA)):
    plt.gca().add_patch(plt.Rectangle((XA[i], YA[i]), (XA[i]+delta-XA[i]), (YA[i]+charlie-YA[i]), linewidth=1.0, edgecolor='r', facecolor='none'))
for i in range(len(XB)):
    plt.gca().add_patch(plt.Rectangle((XB[i], YB[i]), (XB[i]+delta-XB[i]), (YB[i]+charlie-YB[i]), linewidth=1.0, edgecolor='k', facecolor='none'))
for i in range(len(XD)):
    plt.gca().add_patch(plt.Rectangle((XD[i], YD[i]), (XD[i]+delta-XD[i]), (YD[i]+charlie-YD[i]), linewidth=1.0, edgecolor='g', facecolor='none'))
for i in range(len(XE)):
    plt.gca().add_patch(plt.Rectangle((XE[i], YE[i]), (XE[i]+delta-XE[i]), (YE[i]+charlie-YE[i]), linewidth=1.0, edgecolor='b', facecolor='none'))
for i in range(len(XP)):
    plt.gca().add_patch(plt.Rectangle((XP[i], YP[i]), (XP[i]+delta-XP[i]), (YP[i]+charlie-YP[i]), linewidth=1.0, edgecolor='c', facecolor='none'))
for i in range(len(XS)):
    plt.gca().add_patch(plt.Rectangle((XS[i], YS[i]), (XS[i]+delta-XS[i]), (YS[i]+charlie-YS[i]), linewidth=1.0, edgecolor='y', facecolor='none'))
for i in range(len(XU)):
    plt.gca().add_patch(plt.Rectangle((XU[i], YU[i]), (XU[i]+delta-XU[i]), (YU[i]+charlie-YU[i]), linewidth=1.0, edgecolor='m', facecolor='none'))

plt.show() #Shows the image

datacube = np.transpose(datacube, (1, 0, 2))  #transpose to (W, H, C) -> (H, W, C) for visuals


####################################################################################
# Dish selection (Case structure)
####################################################################################

for i in range(len(XA)): # Arthropod coordinates
    A_data=get_spectrum(XA[i],XA[i]+delta,YA[i],YA[i]+delta) #extracting the spectrum
    A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
    A_plot = plt.plot(axis_l,A_data, color = 'r') 
for i in range(len(XB)): # Belt coordinates
    A_data=get_spectrum(XB[i],XB[i]+delta,YB[i],YB[i]+delta) #extracting the spectrum
    A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
    A_plot = plt.plot(axis_l,A_data, color = 'k') 
for i in range(len(XD)): # Dirt coordinates
    A_data=get_spectrum(XD[i],XD[i]+delta,YD[i],YD[i]+delta) #extracting the spectrum
    A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
    A_plot = plt.plot(axis_l,A_data, color = 'g') 
for i in range(len(XE)): # Ethanol coordinates
    A_data=get_spectrum(XE[i],XE[i]+delta,YE[i],YE[i]+delta) #extracting the spectrum
    A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
    A_plot = plt.plot(axis_l,A_data, color = 'b')
for i in range(len(XP)): # Plant coordinates
    A_data=get_spectrum(XP[i],XP[i]+delta,YP[i],YP[i]+delta) #extracting the spectrum
    A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
    A_plot = plt.plot(axis_l,A_data, color = 'c') 
for i in range(len(XS)): # Stone and rock coordinates
    A_data=get_spectrum(XS[i],XS[i]+delta,YS[i],YS[i]+delta) #extracting the spectrum
    A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
    A_plot = plt.plot(axis_l,A_data, color = 'y') 
for i in range(len(XU)): # objects that are not clear to identify or unidentified by design
    A_data=get_spectrum(XU[i],XU[i]+delta,YU[i],YU[i]+delta) #extracting the spectrum
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