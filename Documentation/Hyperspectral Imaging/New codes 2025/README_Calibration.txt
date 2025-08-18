Here's a step-by-step breakdown of what will happen when you run the program:


🧭 1. Load Hyperspectral Image Data
It will read the .bin file from:
C:/Users/mariu/Desktop/HC Data/2022-10-5_12-49-42_1296x1000x900_imageCube.bin
The file is expected to have dimensions: [900 bands, 1000 lines, 1296 pixels].

It reshapes and transposes the data into a cube: [x, y, wavelength].



🟦 2. (Optional) Display the Calibration Board Layout
If SanityBoard = True, it will:

Show a grayscale image of the scene at a specific wavelength (channel = 630)

Overlay rectangles for:

White reference panel

Blue calibration squares (X) (belt driving dir.)

Green calibration stripes (Y) (across belt)

LED positions

✅ Useful to verify that your positions and coordinates are correct.



🔬 3. Extract and Save White Reference
Averages the intensities in the white reference area (along the x-axis).

Produces a 2D array: [y, spectral bands]

Saves it to a .csv file:
WhiteCalibration_VIS_NIR_"date".csv
at the created folder:
output_path = os.path.join(folder, date_time, f"Calibration_{date}/") 
If SanityLED = True, you'll also see a plot of the average white spectrum.



📏 4. Perform Spatial Calibration
🔹 X-direction (Blue squares)
Scans across 14 blue squares spaced vertically.

Detects bright/dark transitions (square boundaries).

Calculates average square width in pixels.

Converts it to millimeters using the known physical width (15 mm).

Derives X_coeff = mm/pixel.

🔹 Y-direction (Green stripes)
Same logic, but horizontally across green stripes.

Derives Y_coeff = mm/pixel.

Result: [X_coeff, Y_coeff] is stored.

If SanitySpatial = True, you'll get plots of square widths in X and Y for inspection.



🌈 5. Perform Wavelength Calibration
Loops over selected LEDs in position_dict.

Extracts each LED’s patch and averages the spectrum.

Detects the peak channel within the expected range.

Matches this with the true wavelength from peak_ref_dict.

Then:

Performs linear regression: wavelength = m × channel + b

Saves b (intercept) and m (slope) as wavelength calibration.

If SanityCali = True, you'll see a scatter plot and fit line showing how well the calibration performs.



💾 6. Save Calibration Coefficients
A final 2×2 CSV file is saved as:
Calibration_coeffs_"date".csv
It includes:

x/intercept	y/slope
Spatial	X_coeff	Y_coeff
wl	intercept	slope



✅ Summary of What You Get After Running
White reference spectrum CSV

Calibration coefficients CSV

Optional visual plots depending on sanity flags

A calibrated data cube ready for reflectance conversion and scientific use



🛑 If Something Fails
Make sure the .bin file exists at the path you defined.

Make sure all AOIs are inside the image bounds.

If LEDs or squares aren’t detected properly, use SanityBoard = True to debug placement visually.

Would you like to add an auto-check to confirm the file exists before proceeding? Or convert this into a script you can run from the command line with arguments (e.g., --date 240101)?