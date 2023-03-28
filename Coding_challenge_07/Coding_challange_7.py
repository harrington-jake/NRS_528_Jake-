# Coding Challenge 7
# Our coding challenge this week should make use of temporary folders, output folders and file management.
#
# Convert your Coding Challenge 5 exercise to work with temporary folders, os.path.join and glob.glob.
# Do not take too much time on this and if you do not have a working Challenge 5, talk to the instructor.

#First I import the necessary packages.
import arcpy
import csv
import os
import glob
arcpy.env.overwriteOutput = True

#Set up your workspace, this will be unique to each user, and should be location where you have your species data.
# For our example, ‘Species_occurrence.csv’ should be in this location.
input_directory = r"C:\NRS\Coding_challanges\Coding_challange_07"
data_file = "Species_occurrence.csv"

if not os.path.exists(os.path.join(input_directory, "temporary_files")):
    os.mkdir(os.path.join(input_directory, "temporary_files"))
if not os.path.exists(os.path.join(input_directory, "outputs")):
    os.mkdir(os.path.join(input_directory, "outputs"))

#Create a list of all the speices (as listed in the 1st column in the CSV file).
species = []
with open(os.path.join(input_directory, data_file)) as spec_occ:
    csv_reader = csv.reader(spec_occ, delimiter=',')
    next(spec_occ) #skip first line
    for row in csv_reader:
        if row[0] not in species:
            species.append(row[0])
print(species)


#Creates a new csv file for each different species in the primary csv file.
header = "species,decimallongitude,decimallatitude\n"
for animal in species:
    animal_count = 1
    with open(r"Species_occurrence.csv") as spec_occ:
        for row in csv.reader(spec_occ):
            if row[0] == animal:
                if animal_count == 1:
                    file = open(str(animal) + ".csv", "w")
                    file.write(header)
                    animal_count = 0
                # make well formmated line
                file.write(",".join(row))
                file.write("\n")
    file.close()

#Converts each new csv file into a shapefile:
    in_Table = str(animal) + ".csv"
    x_coords = "decimallongitude"
    y_coords = "decimallatitude"
    z_coords = ""
    out_Layer = str(animal)
    saved_Layer = animal + '_shapefile.shp'
    # Set the spatial reference
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
    arcpy.CopyFeatures_management(lyr, os.path.join(input_directory, "temporary_files",saved_Layer))
    if arcpy.Exists(animal + '_shapefile.shp') == True:
        print("Shapefile for " + animal + " was created")

os.chdir(os.path.join(input_directory, "temporary_files"))# same as env.workspace
arcpy.env.workspace = os.path.join(input_directory, "temporary_files")
species_file_list = glob.glob("*.shp")# Find all CSV files

for animal in species_file_list:
# Extact the Extent, i.e. XMin, XMax, YMin, YMax of the shapefile:

    desc = arcpy.Describe(animal)
    print(animal + " Y min: %d" % float(desc.extent.YMin))
    print(animal + " Y max: %d" % float(desc.extent.YMax))
    print(animal + " X min: %d" % float(desc.extent.XMin))
    print(animal + " X max: %d" % float(desc.extent.XMax))
    due_north = desc.extent.YMin + int(1) # I'll use this to set the y-Axis of the fishnet directly north.
#
#
#Create a fishnet for each species:
    outFeatureClass = animal.split("_")[0] + "_Fishnet.shp"  # Name of output fishnet
    originCoordinate = str(desc.extent.XMin) + ' ' + str(desc.extent.YMin)   # Left bottom of our point data
    yAxisCoordinate = str(desc.extent.XMin) + ' ' + str(due_north)  # This sets the orientation on the y-axis, so we head north
    cellSizeWidth = (desc.extent.XMax - desc.extent.XMin)/19 #We created a 20x20 fishnet based on the spatial extent of our data.
    cellSizeHeight = (desc.extent.YMax - desc.extent.YMin)/19
    numRows = ""  # Leave blank, as we have set cellSize
    numColumns = ""  # Leave blank, as we have set cellSize
    oppositeCorner = str(desc.extent.XMax) + ' ' + str(desc.extent.YMax)  # i.e. max x and max y coordinate
    labels = "NO_LABELS"
    templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
    geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                   cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                   oppositeCorner, labels, templateExtent, geometryType)
    if arcpy.Exists(animal.split("_")[0] + '_fishnet.shp') == True:
        print("Fishnet for " + animal + " was created")
#
    arcpy.env.workspace = os.path.join(input_directory, "outputs")

    target_features = animal.split("_")[0] + "_Fishnet.shp"
    join_features = animal
    out_feature_class = animal.split("_")[0] + "_HeatMap.shp"
    join_operation="JOIN_ONE_TO_ONE"
    join_type="KEEP_ALL"
    field_mapping=""
    match_option="INTERSECT"
    search_radius=""
    distance_field_name=""
#
    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)
    if arcpy.Exists(animal.split("_")[0] + '_HeatMap.shp') == True:
        print("Heatmap for " + animal + " was created.")
#
# #Remove files we no longer need:
arcpy.Delete_management(os.path.join(input_directory, "temporary_files"))