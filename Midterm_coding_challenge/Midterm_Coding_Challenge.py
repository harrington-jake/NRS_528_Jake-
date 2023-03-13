# -*- coding: utf-8 -*-
"""

"""
#This script is designed to use NOAA Coastal Change Analysis Program (C-CAP) landcover datasets to visualize wetland
# landcover change over a range of timesteps. The code automates this process for as many datasets as the user inputs.
# Note that the example datasets are for Nauset Bay, Cape Cod, and use the UTM 19N projected coordinate system.
# When visualizing this example data in ARCGIS I recommend setting the basemap to UTM 19N.

import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy.management import *
import os

#Define your workspace. (line 18) This path MUST be changed to the location of the data on your machine.
#Be careful here, make sure the workspace path you designate is the directory containing the "Land_cover_rasters" directory.
workspace = r'C:\NRS\Midterm_challenge' #CHANGE THIS!
arcpy.env.workspace = os.path.join(workspace, "Land_Cover_rasters") #"Land_cover_rasters" must contain all the rasters you want to compare.

# Below we automatically select all the rasters in our directory for the analysis.
#If the user only wants to use certain files, they may be listed manually.
initial_timesteps = arcpy.ListRasters("*", "IMG")
end_timesteps = arcpy.ListRasters("*", "IMG")

# Allow overwriting outputs:
arcpy.env.overwriteOutput = True


#Before we apply any GIS tools, we need to set up couple loops using 2 lists. The first list (end_timesteps) Is all the
# datasets you want to serve as the end timestep for each marsh area change analysis. The second list, (initial_timesteps)
# is all the datasets you want to serve as the starting timestep for each change analysis.

#Using the example I provided, these loops will create a new raster showing the change in marsh area for:
# 1996-2001, 1996-2006, 1996-2010, 1996-2016, 2001-2006, 2001-2010, 2001-2016, 2006-2010, 2006-2016, and 2010-2016.

for file in end_timesteps:
    enddate_path = file
    enddate_raster = arcpy.Raster(file)
    end_year = file.split('_')[1]


    for raster in initial_timesteps:
        startdate_raster = arcpy.Raster(raster)
        start_year = raster.split('_')[1]
        if int(start_year) < int(end_year):
            print("Starting process for: " + start_year + '-' + end_year)

#

        #Step 1: Reclassify
        #   In this step we reclassify selected pixel values. In this case, since we are testing for Marsh change,
            # we reclassify all pixel values associated with wetland/estuarine land types (pixel values 13-18:
            # see https://coast.noaa.gov/data/digitalcoast/pdf/ccap-class-scheme-regional.pdf).
            # All wetland land types for the start date are converted to a pixel value of 100. All wetland land types for the
            # end date are converted to a pixel value of 200. We do this so after we sum the pixel values of the 2 rasters in the
            # next step, pixel values of 300 will indicate no marsh change, values between 100-200 will indicate marsh loss, and
            # values between 200-300 will indicate marsh gain. Note that if you are interested in changes in a different land type, you would
            #change the value in the remap field to the pixel value associated with the land type you are interested in.
            Reclass_start = "reclass_" + start_year
            arcpy.ddd.Reclassify(in_raster=startdate_raster, reclass_field="Value", remap="13 100;14 100;15 100;16 100;17 100;18 100", out_raster=Reclass_start, missing_values="DATA")
            Reclass_start = arcpy.Raster(Reclass_start)

            Reclass_end = "reclass_" + end_year
            arcpy.ddd.Reclassify(in_raster=enddate_raster, reclass_field="Value", remap="13 200;14 200;15 200;16 200;17 200;18 200", out_raster=Reclass_end, missing_values="DATA")
            Reclass_end = arcpy.Raster(Reclass_end)
            print("Reclassify for " + start_year + "-" + end_year + " done.")

        #Step 2: Plus
            # In this step we add the raster pixel values. As said above, after this is complete pixel values of 300 will
            # indicate no marsh change, values between 100-200 will indicate marsh loss, and
            # values between 200-300 will indicate marsh gain.

            Plus_rasters = "P_" + start_year + "_" + end_year
            Plus = Plus_rasters
            Plus_rasters = arcpy.sa.Plus(in_raster_or_constant1=Reclass_start, in_raster_or_constant2=Reclass_end)
            Plus_rasters.save(Plus)
            print("Raster addition for " + start_year + "-" + end_year + " done.")

        #Before the final step we create a directory called outputs in which we will store all the newly created rasters.
            if not os.path.exists(os.path.join(workspace, "outputs")):
                os.mkdir(os.path.join(workspace, "outputs"))

        #Step 3: Set Null:
            # In this step, we set any pixel value less than 100 to NULL. remember, any pixel value less than 100 at this point was never a wetland
            #land type, so to make things easier to see in ARCGIS, we set all these pixel values to NULL since we're not interested in them.
            #We then save these final datasets to the new outputs directory.
            Marsh_change = r"outputs\Marsh_change" + start_year + "_" + end_year + ".tif"
            Set_Null = Marsh_change
            Marsh_change = arcpy.sa.SetNull(in_conditional_raster=Plus_rasters, in_false_raster_or_constant=Plus_rasters, where_clause="Value < 100")
            Marsh_change.save(Set_Null)
            print("Irrelevant landcover types removed for " + start_year + "_" + end_year)

        #Step 4:
            #For cleanliness we will now remove any unnecessary intermediate files created during the loop.
            arcpy.Delete_management("reclass_" + start_year)
            arcpy.Delete_management("reclass_" + end_year)
            arcpy.Delete_management("P_" + start_year + "_" + end_year)
            print("Intermediate files for " + start_year + "_" + end_year + " removed")
        print("--\n--\n--")
#


