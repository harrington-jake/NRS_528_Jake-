# In this coding challenge, your objective is to utilize the arcpy.da module to undertake some basic partitioning of
# your dataset. In this coding challenge, I want you to work with the Forest Health Works dataset from RI GIS
# (I have provided this as a downloadable ZIP file in this repository).
# Using the arcpy.da module (yes, there are other ways and better tools to do this), I want you to extract all sites
# that have a photo of the invasive species (Field: PHOTO) into a new Shapefile, and do some basic counts of the dataset.
# In summary, please addressing the following:
# Count how many individual records have photos, and how many do not (2 numbers), print the results.
# Count how many unique species there are in the dataset, print the result.
# Generate two shapefiles, one with photos and the other without.

import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\NRS\Coding_challanges\Coding_challange_09"

input_shp = r"RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
fields = ['Species', 'Other', 'SHAPE@XY']

#Section 1: Count records with and without photos:

expression = arcpy.AddFieldDelimiters(input_shp, "Other") + " = 'PHOTO'" + " OR "
expression = expression + arcpy.AddFieldDelimiters(input_shp, "Other") + " = 'Photo'"

photo_count = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        photo_count += 1

print("There are " + str(photo_count) + " records with photos.")

expression2 = arcpy.AddFieldDelimiters(input_shp, "Other") + " <> 'PHOTO'" + " AND "
expression2 = expression2 + arcpy.AddFieldDelimiters(input_shp, "Other") + " <> 'Photo'" #+ " OR "


No_photo_count = 0
with arcpy.da.SearchCursor(input_shp, fields, expression2) as cursor:
    for row in cursor:
        No_photo_count += 1

print("There are " + str(No_photo_count) + " records without photos.")


#Section 2: Count number of unique species:

unique_species = []
with arcpy.da.SearchCursor(input_shp, fields) as cursor:
    for row in cursor:
        if row[0] not in unique_species:
            unique_species.append(row[0])
num_species = len(unique_species) - 1 # subtracting 1 because the 1st value in the list was blank, so not really a unique species name.
print("There are " + str(num_species) + " Unique Species in this dataset.")


# Section 3: Generate two shapefiles, one with photos and the other without.

out_path = arcpy.env.workspace
out_name = "RI_invasive_photos.shp"
geometry_type = "POINT"
template = r"RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
has_m = "DISABLED"
has_z = "DISABLED"
spatial_ref = 4326

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)
OutputFeature = os.path.join(out_path, out_name)

print("Generating new shapefiles...")
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        with arcpy.da.InsertCursor(OutputFeature, fields) as cur:
            cur.insertRow(row)

print("working on it...")

out_path = arcpy.env.workspace
out_name = "RI_invasive_NO_photos.shp"
geometry_type = "POINT"
template = r"RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
has_m = "DISABLED"
has_z = "DISABLED"
spatial_ref = 4326

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)
OutputFeature2 = os.path.join(out_path, out_name)

with arcpy.da.SearchCursor(input_shp, fields, expression2) as cursor:
    for row in cursor:
        with arcpy.da.InsertCursor(OutputFeature2, fields) as cur:
            cur.insertRow(row)



