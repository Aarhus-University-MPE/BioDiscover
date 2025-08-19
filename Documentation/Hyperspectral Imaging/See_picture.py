# This code is part of a script that processes hyperspectral imaging data.
# It integrates spectral data over specified wavelength ranges and calculates ratios for analysis.


#User input
path='C:/Projects/BioDiscover/Documentation/Hyperspectral Imaging/External files/Billeder 2023/Billede pakker/Originals/' #Where the datacubes are placed ''= next to the script.

'''Change between files as needed'''
#filename = '2022-10-5_12-49-42_1296x1000x900_imageCube' #0
#filename = '2022-10-5_12-51-3_1296x1000x900_imageCube' #1
#filename = '2022-10-5_12-52-13_1296x1000x900_imageCube' #2
#filename = '2022-10-5_12-53-57_1296x1000x900_imageCube' #3
#filename = '2022-10-5_12-54-50_1296x1000x900_imageCube' #4
#filename = '2022-10-5_12-55-39_1296x1000x900_imageCube' #5
filename = '2022-10-5_12-57-43_1296x1000x900_imageCube' #6
#filename = '2022-10-5_12-58-31_1296x1000x900_imageCube' #7
#filename = '2022-10-5_12-59-26_1296x1000x900_imageCube' #8

chanal = 497 #Channal to visualize | 1,42*chanal+513 nm | Important for user to be able to see what is in picture

#importing python packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def get_spectrum(x1,x2,y1,y2): #plotting the average spectrum of the pixels in the selection
    spectrum = datacube[:,y1:y2,x1:x2]
    spectrum = np.mean(spectrum,axis=1)
    spectrum = np.mean(spectrum,axis=1)
    return spectrum

extension='.bin' #Deafult file extension - yes they are binary
indfile= path+filename+extension #Making the finename with path and extension
data = np.fromfile(indfile,  dtype=np.uint8)   #importing filename to data

#These values can be obtaind from the file size or name - to be done
Width = 1296 #Across convayer belt (y)
Length = 1000 #Number of lines scaned (x)
Chanals = 900 #Number of chanals (z, lambda)
datacube = np.reshape(data,(Chanals,Length,Width))    #reshaping from vector to cube

#Figure shoving an image of the datacube
dish = plt.figure() #Initilaization of the figure
plt.xlim(240,945) #cuts image to size; change to fit | 1: (220,920)  2: (225,935)  3: (262,966)  4: (197,903)  5: (311,1010)  6: (240,945)  7: (0, 715)  8: (200,920)
plt.ylim(426,21) #cuts image to size; change to fit | 1: (430,0)  2: (450,47)  3: (435,20)  4: (424,0)  5:(500,115)  6: (426,21)  7: (580,120)  8: (430,0)
plt.imshow(datacube[chanal,:,:],cmap='gray',aspect='auto') #Shows an image of the datacube

wave=1.4234*chanal+513.1 #Wavelength Calibration
plt.title('Wavelength '+str(wave)) #Add name to plot


#''' This part is only for checking if found coordinates are correct | To use put a "#" in front of the three apostrophes in this line
# substitute coordinates with the desired coordinates for a given datafile
X = [366,443,393,424,464,486,503,427,491,481,540,540,568,512,546,578,584,543,571,592,628,612,642,623,625,706,682,717,688,683,733,753,784,812,880]
Y = [116, 72,198,195,182,118,149,235,253,282,224,264,274,310,326, 80,154,183,199,194,226,246,290,120,181, 95,152,137,189,244,220,255,105,190,289]

for i in range(len(X)):
    plt.gca().add_patch(plt.Rectangle((X[i], Y[i]), (X[i]+10-X[i]), (Y[i]+10-Y[i]), linewidth=1.0,edgecolor='r',facecolor='none'))
#'''

# plt.show() 
