# Species Recognition System (SRS)

Software designed to capture and store images of macroinvertebrates using the the SRS system.


# Change log

**v1.9.0.0**
Reworked Detection Algorithm

- Improved version of previous Single Layer Difference Algorithm
- New algorithm uses full RGB layer of image and calibration
- Changed to Absolute Difference calculation into Intensity layer threshold

_Previous Method:_
![](https://github.com/MadsR/BioDiscover/blob/master/Documentation/Detect_Method_1.png)

_New Method:_
![](https://github.com/MadsR/BioDiscover/blob/master/Documentation/Detect_Method_2.png)


**v1.8.0.0**

Reworked GUI

Implemented run-time stats

- Per camera stats
- Mean Area
- Total number of images
- Current sample number

_Minor Changes_

- Reworked Backend
- Changed total number of images to per sample
- Fixed graphical error in Camera number

**v1.7.0.0**

Implemented local camera ID system to support several systems.

*Main Systems*

Modified Camera ID connection algorithm. 
- Check for local ID file > if found > try connection > if failed > request new ID and retry
- If no local ID file is found > request new ID > try connection
- If no file and no connection to micro controller > displays error

*Arduino Changes*

Added Camera ID to Linear Actuator flash.

Added Camera ID request to Linear Actuator Script.
- "108" returns Cam1 ID
- "109" returns Cam2 ID


**v1.6.0.20**

Fixed error with binary filter threshold.

Fixed error with blue plane extract memory allocation

Added detection error in Stats pane

Fixed error with camera view scaling


**v1.6.0.0**

Added new data file (one row per image) containing:
- All original columns (Name, data, operator, etc.).
- Image file name.
- Per image parameters (Max feret, perimeter, area, holes, area + holes).
- ROI descriptor (used for future recalculations of image parameters).


