# Wetland Land Cover Change from CCAP Datasets
This script is designed to use NOAA Coastal Change Analysis Program (C-CAP) landcover datasets to visualize wetland landcover change over a range of timesteps. The code automates this process for as many datasets as the user inputs. Note that the example datasets are for Nauset Bay, Cape Cod, and use the UTM 19N projected coordinate system. When visualizing this example data in ARCGIS I recommend setting the base map to UTM 19N. 

**VERY IMPORTANT**: The variable “workspace” on line 18 must be changed to the appropriate path on each user’s machine. This is the only line of code that MUST be changed. Note that the directory specified in line 18 must also contain the directory called “Land_Cover_rasters”, which in turn contains the raster datasets you are interested in testing for wetland land cover change. 

Additionally, lines 23 and 24 MAY be edited. Currently the code runs the process on every dataset in the “Land_Cover_rasters” folder.  If the user wants to select certain files, those files may be specified in a list on lines 23 and 24. 

For example: currently the “Land_Cover_rasters” folder contains 5 timesteps: 1996, 2001, 2006, 2010, and 2016. The code therefore produces a wetland change raster dataset for 1996-2001, 1996-2006, 1996-2010, 1996-2016, 2001-2006, 2001-2010, 2001-2016, 2006-2010, 2006-2016, and 2010-2016. 

However, if the user specified the following: 

23. initial_timesteps =  [‘Job818688_2001_CCAP.img’, ‘Job818686_2010_CCAP.img’]
24. end_timesteps = [‘Job818685_2016_CCAP.img’] 

The code would only produce outputs for 2001-2016 and 2010-2016

All newly created raster datasets are saved to a new folder in the workspace called “outputs”. 


## ARCGIS processes described below: 

**Step 1: Reclassify:**
       In this step we reclassify selected pixel values. In this case, since we are testing for Marsh change, we reclassify all pixel values associated with wetland/estuarine land types (pixel values 13-18: see https://coast.noaa.gov/data/digitalcoast/pdf/ccap-class-scheme-regional.pdf). All wetland land types for the start date are converted to a pixel value of 100. All wetland land types for the end date are converted to a pixel value of 200. We do this so after we sum the pixel values of the 2 rasters in the next step, pixel values of 300 will indicate no marsh change, values between 100-200 will indicate marsh loss, and values between 200-300 will indicate marsh gain. Note that if you are interested in changes in a different land type, you would change the value in the remap field to the pixel value associated with the land type you are interested in.

**Step 2: Plus:**
        In this step we add the raster pixel values. As said above, after this is complete pixel values of 300 will indicate no marsh change, values between 100-200 will indicate marsh loss, and values between 200-300 will indicate marsh gain.

**Step 3: Set Null:**
         In this step, we set any pixel value less than 100 to NULL. remember, any pixel value less than 100 at this point was never a wetland land type, so to make things easier to see in ARCGIS, we set all these pixel values to NULL since we're not interested in them. We then save these final datasets to the new ‘outputs’ directory.

## Interpreting the output: 

When visualizing the output in GIS, each raster will contain pixel values between 100 and 300. Pixel values 100 – 199 indicate marsh loss, 200 – 299 indicate marsh gain/formation, and 300 indicates marshland present at both timesteps. I recommend adjusting the symbology in ARCGIS to 3 categories to easily visualize where marsh was lost, gained, or remained the same (see image below).  


![marsh_chg_96_16](https://user-images.githubusercontent.com/123588116/224758263-de389c3d-049b-47c0-bef2-ca6a6739ec5b.PNG)

*Example output dataset*
