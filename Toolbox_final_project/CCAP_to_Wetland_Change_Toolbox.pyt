
import arcpy
#arcpy.env.workspace = r"C:\NRS\Coding_challenges\final_project"
arcpy.env.overwriteOutput = True

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [reclassify_CCAP_wetlands, Plus, keep_only_wetlands, CCAP_to_wetland_change]

class reclassify_CCAP_wetlands(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Step 1: Reclassify Wetland values of CCAP datasets"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []
        start_input_raster = arcpy.Parameter(name="start_input_raster",
                                     displayName="Input Raster for Earlier Timestep",
                                     datatype="DERasterDataset",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(start_input_raster)

        end_input_raster = arcpy.Parameter(name="end_input_raster",
                                             displayName="Input Raster for Later Timestep",
                                             datatype="DERasterDataset",
                                             parameterType="Required",  # Required|Optional|Derived
                                             direction="Input",  # Input|Output
                                             )
        params.append(end_input_raster)


        output_raster1 = arcpy.Parameter(name="output1",
                                 displayName="Output for 1st raster",
                                 datatype="DERasterDataset",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output_raster1)

        output_raster2 = arcpy.Parameter(name="output2",
                                         displayName="Output for 2nd raster",
                                         datatype="DERasterDataset",
                                         parameterType="Required",  # Required|Optional|Derived
                                         direction="Output",  # Input|Output
                                         )
        params.append(output_raster2)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        print(len(parameters))
        startdate_raster = parameters[0].valueAsText
        enddate_raster = parameters[1].valueAsText
        reclass_start = parameters[2].valueAsText
        reclass_end = parameters[3].valueAsText

        arcpy.ddd.Reclassify(in_raster=startdate_raster, reclass_field="Value",
                             remap="13 100;14 100;15 100;16 100;17 100;18 100", out_raster=reclass_start,
                             missing_values="DATA")
        reclass_start = arcpy.Raster(reclass_start)


        arcpy.ddd.Reclassify(in_raster=enddate_raster, reclass_field="Value",
                             remap="13 200;14 200;15 200;16 200;17 200;18 200", out_raster=reclass_end,
                             missing_values="DATA")
        reclass_end = arcpy.Raster(reclass_end)

        return

class Plus(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Step 2: Add reclassified rasters"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []
        input_raster1 = arcpy.Parameter(name="input_raster1",
                                     displayName="Input Raster 1",
                                     datatype="DERasterDataset",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_raster1)

        input_raster2 = arcpy.Parameter(name="input_raster2",
                                             displayName="Input Raster 2",
                                             datatype="DERasterDataset",
                                             parameterType="Required",  # Required|Optional|Derived
                                             direction="Input",  # Input|Output
                                             )
        params.append(input_raster2)


        output_raster = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DERasterDataset",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output_raster)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        print(len(parameters))
        input1 = parameters[0].valueAsText
        input2 = parameters[1].valueAsText
        output = parameters[2].valueAsText

        Plus_rasters = arcpy.sa.Plus(in_raster_or_constant1=input1, in_raster_or_constant2=input2)
        Plus_rasters.save(output)

        return

class keep_only_wetlands(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Step 3: Keep only Wetland data"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []
        input_raster = arcpy.Parameter(name="input_raster",
                                        displayName="Input Raster",
                                        datatype="DERasterDataset",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(input_raster)

        output_raster = arcpy.Parameter(name="output",
                                        displayName="Output (include .tif extension)",
                                        datatype="DERasterDataset",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Output",  # Input|Output
                                        )
        params.append(output_raster)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        print(len(parameters))
        input = parameters[0].valueAsText
        output = parameters[1].valueAsText

        Marsh_change = arcpy.sa.SetNull(in_conditional_raster=input, in_false_raster_or_constant=input,
                                        where_clause="Value < 100")
        Marsh_change.save(output)

        return

class CCAP_to_wetland_change(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Wetland Change from CCAP raster"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        params = []

        workspace = arcpy.Parameter(name="workspace",
                                           displayName="File location of Outputs",
                                           datatype="DERasterDataset",
                                           parameterType="Required",  # Required|Optional|Derived
                                           direction="Input",  # Input|Output
                                           )
        params.append(workspace)

        initial_timestep = arcpy.Parameter(name="initial_timestep",
                                     displayName="Input for Earlier Timestep",
                                     datatype="DERasterDataset",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(initial_timestep)

        end_timestep = arcpy.Parameter(name="end_timestep",
                                             displayName="Input for Later Timestep",
                                             datatype="DERasterDataset",
                                             parameterType="Required",  # Required|Optional|Derived
                                             direction="Input",  # Input|Output
                                             )
        params.append(end_timestep)

        final_output = arcpy.Parameter(name="final_output",
                                                displayName="Final Output (include .tif extension)",
                                                datatype="DERasterDataset",
                                                parameterType="Required",  # Required|Optional|Derived
                                                direction="Output",  # Input|Output
                                                )
        params.append(final_output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        print(len(parameters))
        arcpy.env.overwriteOutput = True
        workspace = parameters[0].valueAsText
        initial_timestep = parameters[1].valueAsText
        end_timestep = parameters[2].valueAsText
        final_output = parameters[3].valueAsText
        import os



        arcpy.ddd.Reclassify(in_raster=initial_timestep, reclass_field="Value",
                             remap="13 100;14 100;15 100;16 100;17 100;18 100", out_raster=os.path.join(workspace, "reclass1.tif"),
                             missing_values="DATA")
        reclass1 = arcpy.Raster(os.path.join(workspace, "reclass1.tif"))



        arcpy.ddd.Reclassify(in_raster=end_timestep, reclass_field="Value",
                             remap="13 200;14 200;15 200;16 200;17 200;18 200", out_raster= os.path.join(workspace, "reclass2.tif"),
                             missing_values="DATA")
        reclass2 = arcpy.Raster(os.path.join(workspace, "reclass2.tif"))



        # Step 2: Plus

        Plus_raster = arcpy.sa.Plus(in_raster_or_constant1=reclass1,
                                     in_raster_or_constant2=reclass2)
        Plus_raster.save(os.path.join(workspace, "added_CCAP.tif"))


        # Step 3: Set Null:
        Marsh_change = arcpy.sa.SetNull(in_conditional_raster=Plus_raster,
                                        in_false_raster_or_constant=Plus_raster,
                                        where_clause="Value < 100")
        Marsh_change.save(final_output)

        arcpy.Delete_management(os.path.join(workspace, "reclass1.tif"))
        arcpy.Delete_management(os.path.join(workspace, "reclass2.tif"))
        arcpy.Delete_management(os.path.join(workspace, "added_CCAP.tif"))
        return

