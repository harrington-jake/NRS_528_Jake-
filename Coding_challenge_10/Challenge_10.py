# Our coding challenge this week that improves our practice with rasters from Week 10.
#
# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are interested in
# the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery, see
# here for more info about the bands: https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites. Data
# provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI, and stored
# in the file Landsat_data_lfs.zip.
#
# Before you start, here is a suggested workflow:
#
# 1. Extract the Landsat_data_lfs.zip file into a known location.
# 2. For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool in
# ArcMap and using "Copy as Python Snippet" for the first calculation.

# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your code
# submission, you should also provide a visualization document (e.g. an ArcMap layout in PDF format), showing the
# patterns for an area of RI that you find interesting.

import glob
import os
import arcpy

workspace = r"C:\NRS\Coding_challenges\Coding_challenge_10"
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True


months = (list(filter(os.path.isdir, os.listdir(os.curdir))))
print("Months to be calculated for NVDI: ")
print(months)

for month in months:
    change_dir = (os.path.join(workspace, month))
    os.chdir(change_dir)
    all_tif = glob.glob("*.tif") # list containing all the tif files from the current folder
    needed_bands = []
    for tif in all_tif: # For loop that reduces each list of tif files to bands 4 & 5.
        if tif.split("_")[7] == 'B4.tif' or tif.split("_")[7] == 'B5.tif':
            needed_bands.append(tif)
    print("Bands to be used for NDVI calculation for the month: " + month)
    print(needed_bands)
    Band5 = arcpy.Raster(needed_bands[1])
    Band4 = arcpy.Raster(needed_bands[0])

    NVDI_calc = os.path.join(workspace, month) + "_NVDI"
    Raster_Calculator = NVDI_calc
    NVDI_calc = (Band5 - Band4) / (Band5 + Band4)
    NVDI_calc.save(Raster_Calculator)
    print(month + " finished.")
os.chdir(workspace)




