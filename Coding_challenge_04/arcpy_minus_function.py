# For this coding challenge, I want you to find a particular tool that you like in arcpy. It could be a tool that you have used in GIS before or something new. Try browsing the full tool list to get some insight here (click Tool Reference on the menu list to the left).
#
# Set up the tool to run in Python, add some useful comments, and importantly, provide some example data in your repository (try to make it open source, such as Open Streetmap, or RI GIS. You can add it as a zip file to your repository.
#
# My only requirements are:
#
# Comment your code well.
# Ensure that the code will run on my machine with only a single change to a single variable
# (i.e. a base folder location).


#I have chosen to run the minus tool from the spatial analysis toolbox.
#This tool subtracts the value of the second input raster from the value of the first input raster on a cell-by-cell basis.

#I often use this tool to calculate the elevation change from topographic datasets from different time steps.
#The example data does this type of elevation change calculation on a barrier beach in front of Nauset Bay, Cape Cod, MA.
#This data is freely available at https://coast.noaa.gov/dataviewer/#/lidar/search/


#First import arcpy and the spatial analysis toolbox.
import arcpy
from arcpy.sa import *

#Here I designate my workspace. This is unique to my machine. You will need to change this to whichever location you extracted the .tif files to.
arcpy.env.workspace = r"C:\NRS\Coding_challanges\Coding_challange_04"
#If you prefer, you can delete line 26, and simply make sure to include the full path to each of the raster datasets in lines 35 and 36. 
#For example: r"C:\NRS\Coding_challanges\Coding_challange_04\usace2018_east_cst_Job831130.tif" would work just the same in my case. for line 35. 

#I'm going to allow overwriting the output file so I can test this multiple times without having to keep deleting the output file.
arcpy.env.overwriteOutput = True

# Simply input the two raster datasets you want to use. 
#If you are using the example data i proivded in GitHub, or are doing a similar elevation change analysis, make sure the most
# recent dataset is the 1st input raster, and the older dataset is the 2nd. This way positive values will indicate elevation gain.
inRaster1 = r"usace2018_east_cst_Job831130.tif"
inRaster2 = r"2010_USACE_NE_Job831131.tif"

# Execute Minus
outMinus = Minus(inRaster1, inRaster2)

# Save the output in a location of your choice.
#I have chosen to call my output topo_change, but if you are not calcualting elevation change, different name may be appropriate.
outMinus.save(r"C:\NRS\Coding_challanges\Coding_challange_04\topo_change.tif")
