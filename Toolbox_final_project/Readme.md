# Wetland Change Toolbox

This toolbox has a similar function to the Midterm Challenge python script uploaded to this repository. It uses  NOAA Coastal Change Analysis Program (C-CAP) landcover datasets to visualize wetland landcover change. The toolbox contains 4 tools: one tool for each step in the workflow, and a final tool that does all three steps and deletes any intermediate outputs. Note that while the Midterm python script is designed to analyze marsh change for many different timesteps simultaneously, this toolbox is designed to analyze change only between 2 user-input timesteps of interest.  

Note that all parameters in this toolbox are required. 

For all user-defined output parameters I recommend including a .tif extension at the end. Failing to define the extension may cause errors as you move through the steps of the workflow. 

Each tool and its parameters are described below: 



## **Tool 1** - Step 1: Reclassify Wetland values of CCAP datasets: 

In this step we reclassify selected pixel values. In this case, since we are testing for Marsh change, we reclassify all pixel values associated with wetland/estuarine land types (pixel values 13-18: see https://coast.noaa.gov/data/digitalcoast/pdf/ccap-class-scheme-regional.pdf). All wetland land types for the start date are converted to a pixel value of 100. All wetland land types for the end date are converted to a pixel value of 200. We do this so after we sum the pixel values of the 2 rasters in the next step, pixel values of 300 will indicate no marsh change, values between 100-200 will indicate marsh loss, and values between 200-300 will indicate marsh gain. 

**Parameters:**

  start_input_raster – path to the CCAP raster dataset for the earlier of the two timesteps. 
  
  end_input_raster – path to the CCAP raster dataset for the later of the two timesteps.
  
  output_raster1 – path you want to assign for the reclassified raster of the earlier timestep (wetlands converted to value of 100).  
  
  output_raster2 - path you want to assign for the reclassified raster of the later timestep (wetlands converted to value of 200).  

## **Tool 2** - Step 2: Add Reclassified Rasters: 

In this step we add the raster pixel values. As said above, after this is complete pixel values of 300 will indicate no marsh change, values between 100-200 will indicate marsh loss, and values between 200-300 will indicate marsh gain.

**Parameters:** 

  input_raster1 – Path to the 1st raster you want to add.
  
  input_raster2 - Path to the 2nd raster you want to add.
  
  output_raster - Path you want to assign to the raster created from the addition on the two inputs. 

## **Tool 3** - Step 3: Keep only Wetland Data: 

In this step, we set any pixel value less than 100 to NULL. remember, any pixel value less than 100 at this point was never a wetland land type, so to make things easier to see in ARCGIS, we set all these pixel values to NULL since we're not interested in them. We then save these final datasets to the new ‘outputs’ directory.

**Parameters:**

  Input_raster - Path to the raster created the previous step. 
  
  Output_raster – Path you want to assign to the final raster created after setting pixel values <100 to null.  Make sure to define the extension (.tif) at the end of this parameter. 

## **Tool 4** – Wetland change from CCAP raster: 

Does the three previous steps in succession and deletes intermediate outputs at the end.  

**Parameters:**

  workspace – This parameter is used to store and call the intermediate outputs throughout the workflow. I recommend defining this as the folder where your CCAP datasets are stored (CCAP_example_data if you’re using the example data). 
  
  initial_timestep - Path to the CCAP raster dataset for the earlier of the two timesteps.
  
  end_timestep - Path to the CCAP raster dataset for the later of the two timesteps.
  
  final_output - Path you want to assign to the final raster displaying wetland change. Make sure to define the extension (.tif) at the end of this parameter. 
