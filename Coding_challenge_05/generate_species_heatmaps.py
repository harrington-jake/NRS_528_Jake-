# Coding Challenge 5
# For this coding challenge, I want you to practice the heatmap generation that we went through in class, but this time obtain your own input data, and I want you to generate heatmaps for TWO species.
#
# You can obtain species data from a vast array of different sources, for example:
#
# obis - Note: You should delete many columns (keep species name, lat/lon) as OBIS adds some really long strings that don't fit the Shapefile specification.
# GBIF
# Maybe something on RI GIS
# Or just Google species distribution data
# My requirements are:
#
# The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species (Hint: You can a slightly edited version of our CSV code from a previous session to do this), I recommend downloading the species data from the same source so the columns match.
# Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer, and you provide the species data along with your Python code.
# The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# You leave no trace of execution, except the resulting heatmap files.
# You provide print statements that explain what the code is doing, e.g. Fishnet file generated.




#The data I used for this assignmnet was downloaded from the OBIS data mapper interface (https://mapper.obis.org/).
#The two species mapped are the rabit (Oryctolagus) and coyote (Canis). Due to size considerations, I narrowed my area of study to the state of Rhode Island.
#Despite only using data from Rhode island, I decided to use the spatial refrence WGS 1984, (as opposed to using Rhode Island State plane for example)
#to allow this code to work for data from around the world, and using lat/long coordinates.
#this choice, however, resulted in a bit of inaccuracy in the particular points within my example data. (some points show up of the coast of RI, where you would certainly not find a rabbit or coyote).


#First I import the necessary packages.
import arcpy
arcpy.env.overwriteOutput = True
import csv
import os

#Set up your workspace, this will be unique to each user, and should be location where you have your species data.
# For our example, ‘Species_occurrence.csv’ should be in this location.
arcpy.env.workspace = r"C:\NRS\Coding_challanges\Coding_challange_05"

#Create a list of all the speices (as listed in the 1st column in the CSV file).
species = []
with open(r"Species_occurrence.csv") as spec_occ:
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
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(animal + '_shapefile.shp') == True:
        print("Shapefile for " + animal + " was created")


# Extact the Extent, i.e. XMin, XMax, YMin, YMax of the shapefile:
    desc = arcpy.Describe(animal + '_shapefile.shp')
    print(animal + " Y min: %d" % float(desc.extent.YMin))
    print(animal + " Y max: %d" % float(desc.extent.YMax))
    print(animal + " X min: %d" % float(desc.extent.XMin))
    print(animal + " X max: %d" % float(desc.extent.XMax))
    due_north = desc.extent.YMin + int(1) # I'll use this to set the y-Axis of the fishnet directly north.


#Create a fishnet for each species:
    outFeatureClass = animal + "_Fishnet.shp"  # Name of output fishnet
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
    if arcpy.Exists(animal + '_fishnet.shp') == True:
        print("Fishnet for " + animal + " was created")

    target_features = animal + "_Fishnet.shp"
    join_features = animal + '_shapefile.shp'
    out_feature_class = animal + "_HeatMap.shp"
    join_operation="JOIN_ONE_TO_ONE"
    join_type="KEEP_ALL"
    field_mapping=""
    match_option="INTERSECT"
    search_radius=""
    distance_field_name=""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)
    if arcpy.Exists(animal + '_HeatMap.shp') == True:
        print("Heatmap for " + animal + " was created.")

#Remove files we no longer need:
    os.remove(str(animal) + ".csv")
    arcpy.Delete_management(animal + "_Fishnet.shp")
    arcpy.Delete_management(animal + '_shapefile.shp')

    if arcpy.Exists(animal + '_shapefile.shp') == False:
        print("Shapefile for " + animal + " was deleted")
    if arcpy.Exists(animal + '_fishnet.shp') == False:
        print("Fishnet for " + animal + " was deleted")

