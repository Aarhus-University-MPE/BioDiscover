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
filepath = Path(full_path)

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
verbose=True                # When TRUE: Prints additional information during processing

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
    
   # I am gathering that the line above and one below are from a previus setup with two sensors. For all that I have ssen they could be removed.
   
    #-------------------------------------------
    # Objective values for npy file: image_1.npy
    #-------------------------------------------
    if extension == '.npy':
         # Set calibration regions
        distance = 66*2 #Distance blue square X spacial
        distance2 = 13*2 #Distance green square Y spacial
        
        # AOI for white reference panel (Red zones)
        AOI_white_x1 = 114  # x start value, x = along belt
        AOI_white_x2 = 120 # x width
        AOI_white_y1 = 138  # y start value, y = across belt
        AOI_white_y2 = 1195  # y height
               
       # Blue squares for spatial X calibration
        X_spat_x1 = 62  # x start value, x = along belt
        X_spat_x2 = 112 # x end value
        X_spat_y1 = 72  # y value, y = across belt
        X_spat_y2 = X_spat_y1+66  # y value, y = across belt
        X_min = 25 #minimum x square width
        
        # Green stripes for spatial Y calibration
        Y_spat_x1 = X_spat_x1 # x  value, x = along belt
        Y_spat_x2 = Y_spat_x1 + 12  # x  value, x = along belt
        Y_spat_y1 = X_spat_y1 # y start value, y = across belt
        Y_spat_y2 = 1258 # y end value
        Y_min = 65 #minimum y square width
        
        # LED positions and expected spectral regions
        position_dict = { #tuple of ([x, y], expected peak [channel_min, channel_max]) | Not used LED's are commented out
                    #"LED 1":     ([198, 1190],  [0, 350]),
                    #"LED 2":     ([378, 83],  [0, 350]),
                    #"LED 3":     ([378, 188],   [0, 350]),
                    "LED 4":     ([143, 422],   [0, 150]),
                    "LED 5":     ([143, 515],   [0, 899]),  
                    "LED 6":     ([143, 608],   [50, 899]), 
                    "LED 7":     ([143, 707],   [0, 150]),  
                    "LED 8":     ([143, 802],   [0, 899]),  
                    "LED 9":     ([143, 896],   [0, 899]),  
                    "LED 10":    ([143, 989],   [0, 899]),  
                    "LED 11":    ([143, 1085],   [0, 899]), 
                    #"LED 12":    ([198, 120],   [0, 350]), 
                    #"LED 13":    ([198, 30],    [0, 350]), 
                         
                    #"LED 14":     ([231, 1190], [0, 350]),
                    #"LED 15":     ([420, 83], [0, 899]),
                    "LED 16":     ([158, 324],  [0, 100]),
                    "LED 17":     ([158, 422],  [0, 100]),
                    "LED 18":     ([158, 515],  [0, 200]),
                    "LED 19":     ([158, 609],  [0, 899]), 
                    #"LED 20":     ([420, 623],  [0, 350]),
                    "LED 21":     ([158, 802],  [0, 899]), 
                    "LED 22":     ([158, 897],  [0, 899]),
                    #"LED 23":     ([231, 942],  [0, 350]),
                    "LED 24":     ([156, 1085],  [650, 899]),
                    # "LED 25":    ([231, 120],  [0, 350]),
                    # "LED 26":    ([231, 30],   [0, 350]),
                    }
        
        LED_width = 2
        LED_height = 8
        
       # Load hyperspectral file (.bin or .npy)
        x = 900                 # height (number of lines)
        y = 1392                 # width across belt
        wave = 1044               # number of spectral channels
        expected_shape = (wave, x, y)

    #-------------------------------------------
    # Objective values for bin file: 2022-10-5_12-49-42_1296x1000x900_imageCube.bin
    #-------------------------------------------
    elif extension == '.bin':
        
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
        
        # def load_hyperspectral_file(filepath, expected_shape=None, bin_shape=None, dtype=np.uint8, verbose=True):
        bin_shape = expected_shape  # For .bin files, specify shape as (C, H, W) if known
        dtype=np.uint8
        
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    if verbose:
        print(f"\n🔍 Loading hyperspectral file: {filepath.name}")

    if extension == '.npy':
        datacube = np.load(filepath)

        if not isinstance(datacube, np.ndarray):
            raise ValueError("Loaded .npy file is not a NumPy array.")

        if datacube.ndim != 3:
            raise ValueError(f"Expected 3D array, got shape: {datacube.shape}")

        if verbose:
            print(f"Detected raw shape: {datacube.shape}")

        shape = datacube.shape

        # Map known dimension sizes to roles
        dim_map = {}
        for i, dim in enumerate(shape):
            if dim == 1044:
                dim_map['C'] = i  # spectral channels
            elif dim == 1392:
                dim_map['H'] = i  # along belt (x)
            elif dim == 900:
                dim_map['W'] = i  # across belt (y)
            else:
                raise ValueError(f"Unexpected dimension size {dim} in .npy file.")

        if set(dim_map.keys()) != {'C', 'H', 'W'}:
            raise ValueError(f"Could not detect all required dimensions from shape: {shape}")

        # Step 1: Transpose to (H, W, C)
        transpose_order = [dim_map['H'], dim_map['W'], dim_map['C']]
        datacube = np.transpose(datacube, transpose_order)

        # Step 2: Rotate 90° so H and W are swapped
        datacube = np.rot90(datacube, k=1, axes=(0, 1))
        
        # Step 3: Flip vertically so (0,0) is bottom-left
        datacube = np.flipud(datacube)

        if verbose:        
            print(f"✅ Final shape after rotation: {datacube.shape} (H, W, C)")

    elif extension == '.bin':
        if bin_shape is None:
            raise ValueError("For .bin files, you must provide `bin_shape=(C, H, W)`.")

        expected_size = np.prod(bin_shape)
        actual_size = os.path.getsize(filepath)

        if expected_size != actual_size:
            raise ValueError(f"File size mismatch: expected {expected_size} bytes, got {actual_size} bytes.")

        data = np.fromfile(filepath, dtype=dtype)
        datacube = data.reshape(bin_shape)
        datacube = np.transpose(datacube, (1, 2, 0))  # (C, H, W) → (H, W, C)

        if verbose:
            print(f"Loaded binary file with shape: {datacube.shape}")

    else:
        raise ValueError(f"Unsupported file type: {filepath.suffix}")

    # Final shape check
    if expected_shape:
        if datacube.shape != expected_shape:
            print(f"⚠️ Warning: Image shape {datacube.shape} does not match expected {expected_shape}")
        else:
            if verbose:
                print("✅ Shape matches expected.")

    # return datacube
   
    # ----------------------------------------
    # PLOT CALIBRATION BOARD OVER IMAGE (OPTIONAL)
    # ----------------------------------------
    if SanityBoard:
        datacube = np.transpose(datacube, (1, 0, 2))  #transpose to [y, x, wave] for visuals
        
        if extension == '.npy':
            # Make figure larger and control aspect
            fig, ax = plt.subplots(figsize=(14, 6))  # (width_inches, height_inches)
            ax.imshow(datacube[:, :, channel], cmap='Greys_r', origin="lower", aspect='equal')
            
        elif extension == '.bin':
            fig, ax = plt.subplots(figsize=())  # (width_inches, height_inches)
            ax.imshow(datacube[:, :, channel], cmap='Greys_r', origin="lower", aspect='equal')
        
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

        # Add labels
        ax.set_xlabel('Along conveyer belt')
        ax.set_ylabel('Across conveyer belt')
        
        plt.show()  #show ensures real-time plot
        datacube = np.transpose(datacube, (1, 0, 2))  #tranpose back to [x, y, wave]

    # ----------------------------------------
    # WHITE REFERENCE EXTRACTION AND SAVE
    # ----------------------------------------
    White = datacube[AOI_white_x1:AOI_white_x2, AOI_white_y1:AOI_white_y2, :]
    White = np.mean(White, axis = 0) #The AOI is meaned across x number of lines

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