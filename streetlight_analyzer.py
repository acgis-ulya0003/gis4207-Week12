import arcpy

streetlight_fc = r'..\..\..\..\data\Ottawa\Street_Lights\Street_Lights.shp'
roads_cl_fc = r'..\..\..\..\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
road_name_field = 'ROAD_NAME_'


def _get_unique_values(fc, field_name):
    wsp = fc
    arcpy.env.workspace = wsp
    
    
    rows_list = list()
    

    cursor = arcpy.da.SearchCursor(fc, field_name)

    for row in cursor:
        rows_list.append(row[0])

    unique_rows = set(rows_list)

    return unique_rows

def get_streetlight_count(road_name, distance):

    if road_name in _get_unique_values(roads_cl_fc, 'ROAD_NAME_'):
        

        wsp = roads_cl_fc
        arcpy.env.workspace = wsp

        search_fields = arcpy.AddFieldDelimiters(wsp, 'ROAD_NAME_')
        where_clause = f"{search_fields} = '{road_name}'"
        road = arcpy.management.SelectLayerByAttribute(roads_cl_fc, "NEW_SELECTION", where_clause)
        
        lights = arcpy.management.SelectLayerByLocation(streetlight_fc, 'WITHIN_A_DISTANCE', road, distance)

        count = arcpy.management.GetCount(lights)

        return count
    else:
        print('Road name not found.')
        return None
    

def save_streetlights(road_name, distance, out_fc):
    if road_name in _get_unique_values(roads_cl_fc, road_name_field):
        

        wsp = roads_cl_fc
        arcpy.env.workspace = wsp
        arcpy.env.overwriteOutput = True

        search_fields = arcpy.AddFieldDelimiters(wsp, road_name_field)
        where_clause = f"{search_fields} = '{road_name}'"
        road = arcpy.management.SelectLayerByAttribute(roads_cl_fc, "NEW_SELECTION", where_clause)
        
        lights = arcpy.management.SelectLayerByLocation(streetlight_fc, 'WITHIN_A_DISTANCE', road, distance)
    
        arcpy.management.CopyFeatures(lights, out_fc)

    else:
        print('Road name not found.')
        

    

def show_road_names(pattern=None):
    
    

    wsp = roads_cl_fc
    arcpy.env.workspace = wsp
    
    
    rows_list = list()
    
    if pattern == None:
        cursor = arcpy.da.SearchCursor(roads_cl_fc, 'ROAD_NAME_')
        for row in cursor:
            rows_list.append(row[0])
            
        unique_rows = set(rows_list)
        for i in unique_rows:
            print(i)

    else:
        pattern = pattern.upper()
        search_fields = arcpy.AddFieldDelimiters(wsp, 'ROAD_NAME_')
        where_clause = f"{search_fields} LIKE '%{pattern}%'"

        cursor = arcpy.da.SearchCursor(roads_cl_fc, 'ROAD_NAME_', where_clause)

        for row in cursor:
            rows_list.append(row[0])

        unique_rows = set(rows_list)

        for i in unique_rows:
            print(i)

