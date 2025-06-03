
#User input
path='C:/Users/mariu/Desktop/HC Data/' #Where the datacubes are placed ''= next to the script.

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

chanal = 290 #Channal to visualize approx 1,42*chanal+511 nm exact values is obtained from the calibration board.

'''Coordinates for dish 3'''
XE3 = 430 #Ethanol coordinate
YE3 = 117
XS3 = [361, 381, 497] #Stone and rock coordinates
YS3 = [179, 244, 228]
XP3 = [576, 582, 620] #Plant coordinates
YP3 = [117, 150, 160]
XU3 = [623, 701, 680, 788] #objects that are not clear to identify in the greytone images
YU3 = [74, 114, 163, 143]
XD3 = [650, 683, 743, 783] #Dirt coordinates
YD3 = [275, 297, 272, 256]

'''Coordinates for dish 4'''
XA4 = [254,465,450,403,461,465,494,525,553,605,576,644,585,597,685,699,728,729,863] #Arhtropod coordinates
YA4 = [286, 38, 52,247,268,281,260,241,205,273,355,267,134,157,194,140,101,135,176]
XE4 = 536 #Ethanol coordinate
YE4 = 82
XU4 = [365, 401, 479, 503, 647, 647, 650, 719, 847] #objects that are not clear to identify in the greytone images
YU4 = [137, 187, 133, 218, 147, 111, 216, 60, 260]

'''Coordinates for dish 5 | Used for control'''
XE5 = 393 #Ethanol coordinate
YE5 = 233
XU5 = [476,560,474,508,551,591,612,492,546,259,613,593,616,547,569,613,683,632,649,671,672,660,682,743,700,819,773,799,767,743,793,807,893,880,916] #Objects that intentionally are not pre classified
YU5 = [174,150,255,255,248,195,227,303,320,348,294,340,352,376,400,160,235,264,277,279,313,340,373,216,272,188,244,238,279,334,315,353,206,292,396]

'''Coordinates for dish 6 | Used for control'''
XE6 = 364 #Ethanol coordinate
YE6 = 285
XU6 = [366,443,393,424,464,486,503,427,491,481,540,540,568,512,546,578,584,543,571,592,628,612,642,623,625,706,682,717,688,683,733,753,784,812,880] #Objects that intentionally are not pre classified
YU6 = [116, 72,198,195,182,118,149,235,253,282,224,264,274,310,326, 80,154,183,199,194,226,246,290,120,181, 95,152,137,189,244,220,255,105,190,289]

'''Coordinates for dish 8 | Main data due to having all kinds of matter'''
XA8 = [328,318,447,414,489,487,500,515,523,511,568,585,605,606,604,562,579,548,664,657,642,625,696,307,377,401] #Arthrod coordinates
YA8 = [118,163,213,329,156,193,200,208,217,275,186,113,114,190,211,230,228,313,204,227,256,288,257,292,200,275]
XE8 = 384 #Ethanol coordinate
YE8 = 84
XS8 = [648,764,716] #Stone and rock coordinates
YS8 = [72, 123,291]
XP8 = [318,325,353,338,400,440,483,531,543,595,542,619,776] #Plant coordinates
YP8 = [223,255,265,276,145,157, 82, 74,128,145,243,224,204]

'''Specify wavelengths in virtual filter'''
wave_1 = 980
wave_2 = wave_1 + 10
wave_3 = 1300
wave_4 = wave_3 + 10

#importing python packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

extension='.bin' #Deafult file extension - yeps they are binary
indfile= path+filename+extension #Making the finename with path and extension
data = np.fromfile(indfile,  dtype=np.uint8)   #importing filename to data

#These values can be obtaind from the file size or name - to be done
Width = 1296 #Across convayer belt (y)
Length = 1000 #Number of lines scaned (x)
Chanals = 900 #Number of chanals (z, lambda)

datacube = np.reshape(data,(Chanals,Length,Width))    #reshaping from vector to cube

def get_spectrum(x1,x2,y1,y2): #plotting the average spectrum of the pixels in the selection
    spectrum = datacube[:,y1:y2,x1:x2]
    spectrum = np.mean(spectrum,axis=1)
    spectrum = np.mean(spectrum,axis=1)
    return spectrum

def beregnRatio(x,y,delta):                         #Function which integrates the hyperspectral signature in the filtered ranges and returns the quotient
    A_data = get_spectrum(x,x+delta,y,y+delta)
    res = []
    x_ny = []
    for i in range(0,200):                          
        factor = i/100
        comp_data = A_data-B_data*factor
        fejl = abs(np.average(comp_data))
        res.append(fejl)
        x_ny.append(i/100)
    index = res.index(min(res))                     
    factor = (x_ny[index])                          #gets how much ethanol is in the area, not great with depth, therefor unused for project, but was there for testing

    comp_data = A_data-B_data*factor                #area with ethanol removed by how much ethanol is in the area

    wv = wave_1
    y_intBA = 0
    for i in range(wave_1, wave_2): #integrates in the first virtual filter
        wv = wv + 1
        ff = int((wv - 513.1)/1.4234)
        yy = A_data[ff] 
        y_intBA = y_intBA + yy 

    wv = wave_3
    y_intBB = 0
    for i in range(wave_3, wave_4): #integrates in the second filter
        wv = wv + 1
        ff = int((wv - 513.1)/1.4234)
        yy = A_data[ff] 
        y_intBB = y_intBB + yy 

    A = y_intBA
    B = y_intBB
    R = A/B

    return factor, R


delta = 10          #length and height of area studied

'''Code for individual dishes | Add a number-sign/hashtag in front of the three apostrophes of the dish you wish to work with; just as is at the end of each snippet'''
'''
print("__Stone3__")
for i in range(len(XS3)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE3,XE3+delta,YE3,YE3+delta)
    FA, fb = beregnRatio(XS3[i], YS3[i], delta)
    print(fb)
print("__Plant3__")
for i in range(len(XP3)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE3,XE3+delta,YE3,YE3+delta)
    FA, fb = beregnRatio(XP3[i], YP3[i], delta)
    print(fb)
print("__Unknown3__")
for i in range(len(XU3)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE3,XE3+delta,YE3,YE3+delta)
    FA, fb = beregnRatio(XU3[i], YU3[i], delta)
    print(fb)
print("__Dirt3__")
for i in range(len(XD3)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE3,XE3+delta,YE3,YE3+delta)
    FA, fb = beregnRatio(XD3[i], YD3[i], delta)
    print(fb)
#'''

'''
print("__Animal4__")
for i in range(len(XA4)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE4,XE4+delta,YE4,YE4+delta)
    FA, fb = beregnRatio(XA4[i], YA4[i], delta)
    print(fb)
print("__Unknown4__")
for i in range(len(XU4)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE4,XE4+delta,YE4,YE4+delta)
    FA, fb = beregnRatio(XU4[i], YU4[i], delta)
    print(fb)
#'''

'''
print("__Dish5__")
for i in range(len(XU5)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE5,XE5+delta,YE5,YE5+delta)
    FA, fb = beregnRatio(XU5[i], YU5[i], delta)
    print(fb)
#'''

#'''
print("__Dish6__")
for i in range(len(XU6)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE6,XE6+delta,YE6,YE6+delta)
    FA, fb = beregnRatio(XU6[i], YU6[i], delta)
    print(fb)
#'''

'''
print("__Animal8__")
for i in range(len(XA8)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE8,XE8+delta,YE8,YE8+delta)
    FA, fb = beregnRatio(XA8[i], YA8[i], delta)
    print(fb)
print("__Stone8__")
for i in range(len(XS8)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE8,XE8+delta,YE8,YE8+delta)
    FA, fb = beregnRatio(XS8[i], YS8[i], delta)
    print(fb)
print("__Plant8__")
for i in range(len(XP8)):   #get quotients from filtered ranges
    B_data = get_spectrum(XE8,XE8+delta,YE8,YE8+delta)
    FA, fb = beregnRatio(XP8[i], YP8[i], delta)
    print(fb)
#'''


plt.show()
