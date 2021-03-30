import arcpy

streetlight_fc = r'..\..\data\Ottawa\Street_Lights\Street_Lights.shp'
roads_cl_fc = r'..\..\data\Ottawa\Street_Lights\Road_Centrelines.shp'
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
    pass

def save_streetlights(road_name, distance, out_fc):
    pass

def show_road_names(pattern=None):
    pass

#print(_get_unique_values(streetlight_fc, 'STREET_NAM'))