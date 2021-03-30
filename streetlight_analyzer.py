import arcpy

streetlight_fc = r'..\..\data\Ottawa\Street_Lights\Street_Lights.shp'
roads_cl_fc = r'..\..\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
road_name_field = None


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
        
        #lights, count = arcpy.management.SelectLayerByLocation(streetlight_fc, 'WITHIN_A_DISTANCE', road, distance)
        
        lights = arcpy.management.SelectLayerByLocation(streetlight_fc, 'WITHIN_A_DISTANCE', road, distance)

        count = arcpy.management.GetCount(lights)

        return count
    else:
        print('Road name not found.')
        return None
    

def save_streetlights(road_name, distance, out_fc):
    pass

def show_road_names(pattern=None):
    pass

#print(_get_unique_values(streetlight_fc, 'STREET_NAM'))

#print(get_streetlight_count('CARLING AVE', 0.0002))