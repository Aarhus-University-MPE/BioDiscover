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

#---------------------------
#User input
#---------------------------
path='C:/Projects/BioDiscover/Documentation/Hyperspectral Imaging/External files/Billeder 2023/Billede pakker/Originals/' #Where the datacubes are placed ''= next to the script.

# Sample selection
Selected_Sample = 6   # choose 0–8 [0,2 are not used]
chanal = 290        # channel to visualize

# ---------------------------
# File selection
# ---------------------------
filenames = [
    '2022-10-5_12-49-42_1296x1000x900_imageCube', #0
    '2022-10-5_12-51-3_1296x1000x900_imageCube',  #1
    '2022-10-5_12-52-13_1296x1000x900_imageCube', #2
    '2022-10-5_12-53-57_1296x1000x900_imageCube', #3
    '2022-10-5_12-54-50_1296x1000x900_imageCube', #4
    '2022-10-5_12-55-39_1296x1000x900_imageCube', #5
    '2022-10-5_12-57-43_1296x1000x900_imageCube', #6
    '2022-10-5_12-58-31_1296x1000x900_imageCube', #7
    '2022-10-5_12-59-26_1296x1000x900_imageCube'  #8
]
filename = filenames[Selected_Sample]
print(f"Loading: {filename}")

'''Coordinates for dish 1'''
XB1 = [399,760] #Belt X dish 1
YB1 = [501,842] #Belt Y dish 1
XE1 = [475,650,574] #Ethanol X dish 1
YE1 = [190,250,293] #Ethanol Y dish 1

'''Coordinates for dish 3'''
XE3 = [430, 518] #Ethanol coordinates
YE3 = [117, 92]
XS3 = [361, 381, 497] #Stone and rock coordinates
YS3 = [179, 244, 228]
XP3 = [576, 582, 620] #Plant coordinates
YP3 = [117, 150, 160]
XU3 = [623, 701, 680, 788] #objects that are not clear to identify in the greytone images
YU3 = [74, 114, 163, 143]
XD3 = [650, 683, 743, 783] #Dirt coordinates
YD3 = [275, 297, 272, 256]

'''Coordinates for dish 4'''
XA4 = [254,465,450,403,461,465,494,525,553,605,576,644,585,597,685,699,728,729,863] #Arthropod coordinates
YA4 = [286, 38, 52,247,268,281,260,241,205,273,355,267,134,157,194,140,101,135,176]
XE4 = [536, 766] #Ethanol coordinates
YE4 = [82, 281]
XU4 = [365, 401, 479, 503, 647, 647, 650, 719, 847] #objects that are not clear to identify in the greytone images
YU4 = [137, 187, 133, 218, 147, 111, 216, 60, 260]

'''Coordinates for dish 5 | Used for control'''
XE5 = [393, 735] #Ethanol coordinates
YE5 = [233, 390]
XU5 = [476,560,474,508,551,591,612,492,546,259,613,593,616,547,569,613,683,632,649,671,672,660,682,743,700,819,773,799,767,743,793,807,893,880,916] #Objects that intentionally are not pre classified
YU5 = [174,150,255,255,248,195,227,303,320,348,294,340,352,376,400,160,235,264,277,279,313,340,373,216,272,188,244,238,279,334,315,353,206,292,396]

'''Coordinates for dish 6 | Used for control'''
XE6 = [364, 820] #Ethanol coordinates
YE6 = [285, 131]
XU6 = [366,443,393,424,464,486,503,427,491,481,540,540,568,512,546,578,584,543,571,592,628,612,642,623,625,706,682,717,688,683,733,753,784,812,880] #Objects that intentionally are not pre classified
YU6 = [116, 72,198,195,182,118,149,235,253,282,224,264,274,310,326, 80,154,183,199,194,226,246,290,120,181, 95,152,137,189,244,220,255,105,190,289]

'''Coordinates for dish 7'''
XB7 = [190,522] #Belt X dish 7
YB7 = [66, 626] #Belt Y dish 7
XE7 = [273,368,574] #Empty X dish 7
YE7 = [263,233,360] #Empty y dish 7

'''Coordinates for dish 8 | Main data due to having all kinds of matter'''
XA8 = [328,318,447,414,489,487,500,515,523,511,568,585,605,606,604,562,579,548,664,657,642,625,696,307,377,401] #Arthropod coordinates
YA8 = [118,163,213,329,156,193,200,208,217,275,186,113,114,190,211,230,228,313,204,227,256,288,257,292,200,275]
XE8 = [384,798, 702] #Ethanol coordinates
YE8 = [84, 267, 114]
XS8 = [648,764,716] #Stone and rock coordinates
YS8 = [72, 123,291]
XP8 = [318,325,353,338,400,440,483,531,543,595,542,619,776] #Plant coordinates
YP8 = [223,255,265,276,145,157, 82, 74,128,145,243,224,204]

#---------------------------
#importing python packages
#---------------------------
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.patches import Rectangle
from pathlib import Path

#---------------------------
#plotting the average spectrum of the pixels in the selection
#---------------------------
def get_spectrum(x1,x2,y1,y2): 
    spectrum = datacube[:,y1:y2,x1:x2]
    spectrum = np.mean(spectrum,axis=1)
    spectrum = np.mean(spectrum,axis=1)
    return spectrum

extension ='.bin' #Deafult file extension - yeps they are binary
file = os.path.join(path + filename + extension) #Making the finename with path and extension
print (f"Loading data from: {file}")
data = np.fromfile(file,  dtype=np.uint8)   #importing filename to data

#---------------------------
# Data cupe size (These values can be obtaind from the file size or name)
#---------------------------
Width = 1296 #Across convayer belt (y)
Length = 1000 #Number of lines scaned (x)
Chanals = 900 #Number of chanals (z, lambda)
datacube = np.reshape(data,(Chanals,Length,Width))    #reshaping from vector to cube

#Figure shoving an image of the datacube
dish = plt.figure() #Initilaization of the figure
#plt.xlim(240,945) #cuts image to size; change to fit | 1: (220,920)  2: (225,935)  3: (262,966)  4: (197,903)  5: (311,1010)  6: (240,945)  7: (0, 715)  8: (200,920)
#plt.ylim(426,21) #cuts image to size; change to fit | 1: (430,0)  2: (450,47)  3: (435,20)  4: (424,0)  5:(500,115)  6: (426,21)  7: (580,120)  8: (430,0)
plt.imshow(datacube[chanal,:,:],cmap='gray',aspect='auto') #Shows an image of the datacube
plt.title(f'Dish {Selected_Sample} | Channel {chanal}') #Add name to plot

plt.show() #Shows the image

#---------------------------
#Wavelength calibration 
#---------------------------
A = 1.4234 #Calibration factor
B = 513.1 #Calibration offset
axis_l = np.arange(900)*A+B      #creating band-wavelength table
delta=5

#------------------------------------------------------------------------------
# Dish selection (Case structure)
#------------------------------------------------------------------------------
match Selected_Sample:
    case 1:
        for i in range(len(XB1)):
            A_data=get_spectrum(XB1[i],XB1[i]+delta,YB1[i],YB1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k') 
        for i in range(len(XE1)):
            A_data=get_spectrum(XE1[i],XE1[i]+delta,YE1[i],YE1[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')

    case 3:
        for i in range(len(XD3)):
            A_data=get_spectrum(XD3[i],XD3[i]+delta,YD3[i],YD3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k')
        for i in range(len(XS3)):
            A_data=get_spectrum(XS3[i],XS3[i]+delta,YS3[i],YS3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k')
        for i in range(len(XU3)):
            A_data=get_spectrum(XU3[i],XU3[i]+delta,YU3[i],YU3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r')
        for i in range(len(XP3)):
            A_data=get_spectrum(XP3[i],XP3[i]+delta,YP3[i],YP3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g')
        for i in range(len(XE3)):
            A_data=get_spectrum(XE3[i],XE3[i]+delta,YE3[i],YE3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')

    case 4:
        for i in range(len(XA4)):
            A_data=get_spectrum(XA4[i],XA4[i]+delta,YA4[i],YA4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r')
        for i in range(len(XU4)):
            A_data=get_spectrum(XU4[i],XU4[i]+delta,YU4[i],YU4[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k')
        for i in range(len(XE3)):
            A_data=get_spectrum(XE3[i],XE3[i]+delta,YE3[i],YE3[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')

    case 5:
        for i in range(len(XU5)):
            A_data=get_spectrum(XU5[i],XU5[i]+delta,YU5[i],YU5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r')
        for i in range(len(XE5)):
            A_data=get_spectrum(XE5[i],XE5[i]+delta,YE5[i],YE5[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')

    case 6:
        for i in range(len(XU6)):
            A_data=get_spectrum(XU6[i],XU6[i]+delta,YU6[i],YU6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r')
        for i in range(len(XE6)):
            A_data=get_spectrum(XE6[i],XE6[i]+delta,YE6[i],YE6[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')

    case 7:
        for i in range(len(XB7)):
            A_data=get_spectrum(XB7[i],XB7[i]+delta,YB7[i],YB7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k')
        for i in range(len(XE7)):
            A_data=get_spectrum(XE7[i],XE7[i]+delta,YE7[i],YE7[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')

    case 8:
        for i in range(len(XA8)):
            A_data=get_spectrum(XA8[i],XA8[i]+delta,YA8[i],YA8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'r')
        for i in range(len(XP8)):
            A_data=get_spectrum(XP8[i],XP8[i]+delta,YP8[i],YP8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'g')
        for i in range(len(XS8)):
            A_data=get_spectrum(XS8[i],XS8[i]+delta,YS8[i],YS8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'k')
        for i in range(len(XE8)):
            A_data=get_spectrum(XE8[i],XE8[i]+delta,YE8[i],YE8[i]+delta) #extracting the spectrum
            A_data = (A_data - min(A_data))/(max(A_data) - min(A_data)) #fits spectrum between 0 and 1
            A_plot = plt.plot(axis_l,A_data, color = 'b')

title = "Collected Spectrum of dish " + str(Selected_Sample)
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