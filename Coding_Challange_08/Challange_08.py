# Our coding challenge this week follows from the last exercise that we did in class during Week 8 where we worked with functions.
#
# Convert some of your earlier code into a function. The only rules are: 1) You must do more than one thing to your input
# to the function, and 2) the function must take two arguments or more. You must also, 3) provide a zip file of example data within your repo.
#
# Plan the task to take an hour or two, so use one of the simpler examples from our past classes.


import arcpy
import os
from arcpy.sa import *
arcpy.env.overwriteOutput = True

#Here I designate my workspace. You will need to change this to whichever location you extracted the .tif files to.
workspace = r"C:\NRS\Coding_challanges\Coding_challange_08"
arcpy.env.workspace = workspace


# The following function preforms the minus function (similar to my code for challenge 4), then uses the set null tool
# to remove pixel values greater than 0. This creates a raster indication only areas of elevation loss (erosion)
# between two elevation raster datasets from different time steps.

def Erosion(inRaster1, inRaster2):
    # Execute Minus
    outMinus = Minus(inRaster1, inRaster2)
    outMinus.save(os.path.join(workspace, "Topo_change"))

    Erosion = r"Erosion.tif"
    Set_Null = Erosion
    Erosion = arcpy.sa.SetNull(in_conditional_raster=outMinus, in_false_raster_or_constant=outMinus, where_clause="Value > 0")
    Erosion.save(Set_Null)
    return



#Here we define the raster files to use, the younger data must be raster 1 and the older timestep, raster 2, so that
#negative values indicate a loss of elevation.
inRaster1 = r"usace2018_east_cst_Job831130/usace2018_east_cst_Job831130.tif"
inRaster2 = r"2010_USACE_NE_Job831131.tif.aux/2010_USACE_NE_Job831131.tif"
Erosion(inRaster1,inRaster2)
