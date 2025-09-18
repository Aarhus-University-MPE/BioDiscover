# New calibration script for hyperspectral cameras
# This script is designed to calibrate hyperspectral imaging data by in both .bin files and .npy files.
# This script processes hyperspectral imaging data, calibrates spatial and spectral dimensions, and saves the calibration coefficients.
# It includes options for visual sanity checks and outputs calibration coefficients to a CSV file.
# It is designed to work with a specific camera setup and data format.


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

# ----------------------------------------------
# USER INPUT AND BASIC SETUP
# ----------------------------------------------

# === User input: just paste the full file path here ===
full_path_str = r"C:\Projects\BioDiscover\Documentation\Hyperspectral Imaging\External files\Billeder 2024\image_1.npy"

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


# Create a subfolder for storing calibration outputs
if date == "unknown" or time == "unknown":
    Calibration_folder = FileName
else:
    Calibration_folder = date + "_" + time

now = datetime.now()
current_date_time = now.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
output_folder = os.path.join(folder, Calibration_folder, f"Calibration-Date_{current_date_time}")
output_path = os.path.join(output_folder + "/") 
os.makedirs(output_folder, exist_ok=True)
print(f"Calibration results will be saved to: {output_folder}")


# Toggle visual sanity checks
channel = 630              # Chosen channel for image creation
SanityBoard = True         # When TRUE: Shows the calibration board with the calibration boxes overlaid
SanityLED = True           # When TRUE: Shows white reference and spectral signature over each LED
SanitySpatial = True       # When TRUE: Shows pixel length in the x and y directions
SanityCali = True          # When TRUE: Shows regression | Calibration constants for channel to wavelengths conversion

# Calibration output files
CoefficientsFileName = "Calibration_coeffs" + ".csv"
final_coefficients = None #enable an array for the calibration constants
WhiteFileName = "WhiteCalibration_VIS_NIR" + ".csv" #output filename

# Known LED peak wavelengths (based on hardware spec)
peak_ref_dict = { #The right wavelength according to the board
    "LED 1": 0,
    "LED 2": 365,
    "LED 3": 465,
    "LED 4": 596,
    "LED 5": 609,
    "LED 6": 681,
    "LED 7": 597,    
    "LED 8": 861,    
    "LED 9": 960,    
    "LED 10": 1222,
    "LED 11": 1464,
    "LED 12": 0,
    "LED 13": 0,
    
    "LED 14": 0,
    "LED 15": 395,
    "LED 16": 520,
    "LED 17": 573,
    "LED 18": 646,
    "LED 19": 750,   
    "LED 20": 845,   
    "LED 21": 879,   
    "LED 22": 1063,
    "LED 23": 1300,
    "LED 24": 1525,
    "LED 25": 0,
    "LED 26": 0
    }

# -----------------------------------------------------
# LOAD IMAGE CUBE AND DEFINE AOIs (AREAS OF INTEREST)
# -----------------------------------------------------
for i in range(0, 1):
    
    data_format_choice = 0 # Leftover from former setup; there is now only 1 camera chip, not 2 | It works, don't change it
   
   # I am gathering that the two lines above and one below are from a previus setup with two sensors. For all that I have ssen they could be removed.
   
    if data_format_choice == 0:
        # Set calibration regions
        distance = 75*2 #Distance blue square X spacial
        distance2 = 40*2 #Distance green square Y spacial
        
        # AOI for white reference panel (Red zones)
        AOI_white_x1 = 293  # x start value, x = along belt
        AOI_white_x2 = 312 # x width
        AOI_white_y1 = 4  # y start value, y = across belt
        AOI_white_y2 = 1292  # y height
               
       # Blue squares for spatial X calibration
        X_spat_x1 = 130  # x start value, x = along belt
        X_spat_x2 = 287 # x end value
        X_spat_y1 = 60  # y value, y = across belt
        X_spat_y2 = X_spat_y1+73  # y value, y = across belt
        X_min = 25 #minimum x square width
        
        # Green stripes for spatial Y calibration
        Y_spat_x1 = X_spat_x1 # x  value, x = along belt
        Y_spat_x2 = Y_spat_x1 + 40  # x  value, x = along belt
        Y_spat_y1 = X_spat_y1 # y start value, y = across belt
        Y_spat_y2 = 1258 # y end value
        Y_min = 65 #minimum y square width
        
        # LED positions and expected spectral regions
        position_dict = { #tuple of ([x, y], expected peak [channel_min, channel_max]) | Not used LED's are commented out
                    #"LED 1":     ([198, 1190],  [0, 350]),
                    #"LED 2":     ([378, 83],  [0, 350]),
                    #"LED 3":     ([378, 188],   [0, 350]),
                    "LED 4":     ([378, 299],   [0, 150]),
                    "LED 5":     ([378, 404],   [0, 899]),  
                    "LED 6":     ([378, 510],   [50, 899]), 
                    "LED 7":     ([378, 623],   [0, 150]),  
                    "LED 8":     ([378, 728],   [0, 899]),  
                    "LED 9":     ([378, 837],   [0, 899]),  
                    "LED 10":    ([378, 942],   [0, 899]),  
                    "LED 11":    ([383, 1054],   [0, 899]), 
                    #"LED 12":    ([198, 120],   [0, 350]), 
                    #"LED 13":    ([198, 30],    [0, 350]), 
                         
                    #"LED 14":     ([231, 1190], [0, 350]),
                    #"LED 15":     ([420, 83], [0, 899]),
                    "LED 16":     ([420, 188],  [0, 100]),
                    "LED 17":     ([420, 299],  [0, 100]),
                    "LED 18":     ([420, 404],  [0, 200]),
                    "LED 19":     ([420, 510],  [0, 899]), 
                    #"LED 20":     ([420, 623],  [0, 350]),
                    "LED 21":     ([420, 728],  [0, 899]), 
                    "LED 22":     ([420, 837],  [0, 899]),
                    #"LED 23":     ([231, 942],  [0, 350]),
                    "LED 24":     ([420, 1050],  [650, 899]),
                    # "LED 25":    ([231, 120],  [0, 350]),
                    # "LED 26":    ([231, 30],   [0, 350]),
                    }
        
        LED_width = 11
        LED_height = 20
        
       # Load hyperspectral file (.bin or .npy)
        x = 1000                 # height (number of lines)
        y = 1296                 # width across belt
        wave = 900               # number of spectral channels
        expected_shape = (wave, x, y)

        # Check if the file is .npy or .bin
        if full_path_str.endswith('.npy'):
            print("Loading .npy file...")
            datacube = np.load(full_path)
            if datacube.shape != (x, y, wave):
                # If stored in shape (wave, x, y), transpose it
                if datacube.shape == expected_shape:
                    datacube = np.transpose(datacube, (1, 2, 0))
                else:
                    raise ValueError(f"Unexpected shape: {datacube.shape}")
        else:
            print("Loading .bin file...")
            data = np.fromfile(full_path, dtype=np.uint8)
            expected_size = wave * x * y
            if data.size != expected_size:
                raise ValueError(f"File size mismatch. Expected {expected_size}, got {data.size}")
            datacube = data.reshape((wave, x, y))
            datacube = np.transpose(datacube, (1, 2, 0))  # shape to [x, y, wave]

   
    # ----------------------------------------
    # PLOT CALIBRATION BOARD OVER IMAGE (OPTIONAL)
    # ----------------------------------------
    if SanityBoard:
        datacube = np.transpose(datacube, (1, 0, 2))  #transpose to [y, x, wave] for visuals
        fig, ax = plt.subplots()
        ax.imshow(datacube[:, :, channel], cmap='Greys_r', origin="lower")
            # Adding area of interests
        ax.add_patch(Rectangle((AOI_white_x1, AOI_white_y1), # Illustrate the white AOI
                                AOI_white_x2 - AOI_white_x1, AOI_white_y2 - AOI_white_y1,
                                edgecolor='r',facecolor='none'))

        for j in range(0,8):
            ax.add_patch(Rectangle((X_spat_x1, X_spat_y1+distance*j), # Illustrate the spatial AOI
                                X_spat_x2 - X_spat_x1, X_spat_y2 - X_spat_y1,
                                edgecolor='b',facecolor='none'))
        for _ in range(0,2):
            ax.add_patch(Rectangle((Y_spat_x1+distance2*_, Y_spat_y1), # Illustrate the spatial AOI
                                    Y_spat_x2 - Y_spat_x1, Y_spat_y2 - Y_spat_y1,
                                    edgecolor='g',facecolor='none'))
        
        for value in position_dict.values():
            ax.add_patch(Rectangle(
                (value[0][0], value[0][1]), # Illustrate the white AOI
                value[0][0] + LED_width -value[0][0] , value[0][1] + LED_height - value[0][1],
                linewidth=1.0,edgecolor='r',facecolor='none'))

        ax.invert_xaxis()
        if data_format_choice == 0:
         ax.invert_yaxis()
        ax.set_xlabel('Along conveyer belt (Door ->)')
        ax.set_ylabel('Across conveyer belt (Wall ->)')
        plt.show()  #show ensures real-time plot
        datacube = np.transpose(datacube, (1, 0, 2))  #tranpose back to [x, y, wave]

    # ----------------------------------------
    # WHITE REFERENCE EXTRACTION AND SAVE
    # ----------------------------------------
    White = datacube[AOI_white_x1:AOI_white_x2, AOI_white_y1:AOI_white_y2, :]
    White = np.mean(White, axis = 0) #The AOI is meaned across x number of lines

    if data_format_choice != 0:
          """Remove dead pixels manually"""
          """ When you have a black you have bright next to """
          White[60][13] = White[60][15]
          White[61][12] = White[61][11]
          White[61][13] = White[61][15] #Black
          White[61][14] = White[61][16]
          White[62][13] = White[62][15]

          White[94][99] = White[95][99]
          White[94][100] = White[95][100]

          White[123][92] = White[123][90]
          White[124][91] = White[124][89]
          White[124][92] = White[124][90] #Black
          White[124][93] = White[124][94]
          White[125][92] = White[125][90]

          White[142][89] = White[142][90]
          White[143][89] = White[139][89] #Black
          White[143][88] = White[143][87]
          White[143][90] = White[143][91]
          White[144][89] = White[140][89] #Black
          White[144][88] = White[144][87]
          White[144][90] = White[144][91]
          White[145][89] = White[145][90]
          
    # Save white calibration file as integers
    np.savetxt(output_path+ WhiteFileName, White, delimiter=",", fmt="%3.4f")
    print(f"{WhiteFileName} has been saved to {output_folder}")

# Plot White Spec and LEDs Spec
    if SanityLED:
        plt.figure()
        plt.plot(np.mean(White, axis=0))
        plt.xlabel("Channels")
        plt.ylabel("Intensity")
        plt.title("White reference")
        plt.show()
        #plt.close()             

# Spatial calibration
#    datacube = np.divide(datacube, White) #convert to reflectance

# ----------------------------------------
# Spatial X calibration
# ----------------------------------------
    """Find mean areas"""
    X_peaks = []
    for j in range(0,14):
        X_area = datacube[X_spat_x1:X_spat_x2, X_spat_y1+distance*j:X_spat_y2+distance*j, :] #AOI [149,15,110]
        X_mean_area = np.mean(X_area, axis=1) #mean across y, [149,110]
        X_mean_area = np.mean(X_mean_area, axis=1) #mean over the 110 channels [149,]
        
        """Find black/white boundaries"""
        threshold_X = np.mean(X_mean_area, axis = 0)
        for i in range(len(X_mean_area) - 1):
            if X_mean_area[i] > threshold_X and X_mean_area[i + 1] < threshold_X:
                X_peaks.append(i)
            elif X_mean_area[i] < threshold_X and X_mean_area[i + 1] > threshold_X:
                X_peaks.append(i)
    
    """Calculated pixel lengths and remove unwanted boundary indices"""
    X_lengths_pixels = np.diff(X_peaks)
    selected_indices = np.where(X_min < X_lengths_pixels)[0] #Remove unwanted peaks
    X_lengths_pixels = X_lengths_pixels[selected_indices]
    
    """Calculate final coefficients and save them in final array"""
    X_length_pixels = np.mean(X_lengths_pixels)
    X_coeff = 15.0 / X_length_pixels # mm/pixels

# ----------------------------------------
# Spatial Y calibration
# ----------------------------------------
    """Find mean areas"""
    Y_peaks = []
    for _ in range (0,2):
        Y_area = datacube[Y_spat_x1+distance2*_:Y_spat_x2+distance2*_, Y_spat_y1:Y_spat_y2, :] #AOI
        Y_mean_area = np.mean(Y_area, axis=0) #mean across x
        Y_mean_area = np.mean(Y_mean_area, axis=1) #mean over channels
        
        """Find black/white boundaries"""    
        threshold_Y = np.mean(Y_mean_area, axis = 0)
        for i in range(len(Y_mean_area) - 1):
            if Y_mean_area[i] > threshold_Y and Y_mean_area[i + 1] < threshold_Y:
                Y_peaks.append(i)
            elif Y_mean_area[i] < threshold_Y and Y_mean_area[i + 1] > threshold_Y:
                Y_peaks.append(i)
    
    """Calculated pixel lengths and remove unwanted boundary indices"""
    Y_lengths_pixels = np.diff(Y_peaks)
    selected_indices = np.where(Y_min < Y_lengths_pixels)[0]
    Y_lengths_pixels = Y_lengths_pixels[selected_indices]
      
    """Calculate final coefficients and save them in final array"""
    Y_length_pixels = np.mean(Y_lengths_pixels)
    Y_coeff = 15.0 / Y_length_pixels # mm/pixels
    
# Assign spatial coefficients to final_coefficients
    spat_coeff = np.reshape(np.array([X_coeff, Y_coeff]), (1, 2))
    
    if final_coefficients is None:
        final_coefficients = spat_coeff
    else:
        final_coefficients = np.append(final_coefficients, spat_coeff, axis=0)
    
# ----------------------------------------
# PLOT SPATIAL CALIBRATION (OPTIONAL)
# ----------------------------------------
    if SanitySpatial:              
        plt.figure()
        plt.plot([i for i in range(len(X_lengths_pixels))], X_lengths_pixels, 'kX')
        plt.xlabel("Square number")
        plt.ylabel("Square width in pixels")
        plt.title("Comparison of square widths in X")
        plt.show()
        #plt.close()
        
        plt.figure()
        plt.plot([i for i in range(len(Y_lengths_pixels))], Y_lengths_pixels, 'kX')
        plt.xlabel("Square number")
        plt.ylabel("Square width [pixels]")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.yticks(np.arange(min(Y_lengths_pixels), max(Y_lengths_pixels)+1, 1.0))
        plt.title("Comparison of square widths in Y")
        plt.show()
        #plt.close()

# ----------------------------------------
# WAVELENGTH CALIBRATION USING LED PEAKS
# ----------------------------------------
   # Loop over LED positions, calculate spectra, and obtain peak
    peak_index_dict = {}
    for key, value in position_dict.items():
         
        LED_area = datacube[value[0][0]:value[0][0]+LED_width,
                            value[0][1]:value[0][1]+LED_height,
                            :]
        if key == 'LED 11':
            LED_area = datacube[value[0][0]:value[0][0]+6,
                                value[0][1]:value[0][1]+6,
                                :]
        Spec = np.mean(np.mean(LED_area, axis=0), axis=0)
        peak_index = value[1][0] + np.argmax(Spec[value[1][0]:value[1][1]])
        peak_index_dict[key] = peak_index
            
        if SanityLED:
            plt.figure()
            plt.plot(Spec, color="black")
            plt.plot(peak_index_dict[key], Spec[peak_index_dict[key]], "kX")
            plt.xlabel("Channels [-]")
            plt.ylabel("Intensity [-]")
            plt.title(key)
            plt.show()
            #plt.close()
    
    # Ensure data_peak gets paired with correct ref_peak and do lin-reg
    Peaks = []
    for key in position_dict:
        Peaks.append((peak_index_dict[key], peak_ref_dict[key])) #Only keep those of interest with LEDs in
    channel_peaks, wl_peaks = zip(*Peaks)
    channel_peaks = np.array(channel_peaks) #from tuple to int
    wl_peaks  = np.array(wl_peaks) #from tuple to int
    m, b = np.polyfit(channel_peaks,  wl_peaks,  1) #Linear regression, m=slope, b=intercept
    wl_coeffs=[b,m] #Assign the slope and intercept to variable    
    corr = np.corrcoef(channel_peaks,  wl_peaks)[0,1] #calculate the correlation
    fit = np.array([0,wave]) #prepare two points to calculate and show the correlation plot
    
    final_coefficients = np.append(final_coefficients, np.reshape(np.array(wl_coeffs), (1, 2)), axis=0)
    
# ----------------------------------------
# PLOT WAVELENGTH CALIBRATION (OPTIONAL)
# ----------------------------------------
    if SanityCali:
        plt.figure()
        plt.scatter(channel_peaks, wl_peaks, facecolors='none', edgecolors='k')
        plt.plot(fit, fit*m+b, color="k", ls = "dashed") 
        plt.text(wave/2, (max(fit)*m+b), "y = "+str(round(m,4))+"x + "+str(round(b,2))+"\nR$^{2}$ = "+str(round(corr,6)), fontsize=18, horizontalalignment='center', verticalalignment='top')
        plt.xlabel("Channels [-]")
        plt.ylabel("Wavelength [nm]")
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.show()
        # plt.close()
        
# ----------------------------------------
# SAVE CALIBRATION COEFFICIENTS TO CSV
# ----------------------------------------
index = ["Spatial", "wl"]
col = ["x/intercept", "y/slope"]

df = pd.DataFrame(final_coefficients, index=index, columns=col)
df.to_csv(output_path+ CoefficientsFileName, float_format="%2.5g")
print(f"{CoefficientsFileName} has been saved to {output_folder}")

# plt.close('all')