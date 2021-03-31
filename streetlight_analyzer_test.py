import streetlight_analyzer as sa


sa.streetlight_fc = r'..\..\..\..\data\Ottawa\Street_Lights\Street_Lights.shp'
sa.roads_cl_fc = r'..\..\..\..\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
sa.road_name_field = 'ROAD_NAME_'

def test_get_unique_values():
    expected = 8674
    actual = len(sa._get_unique_values(sa.roads_cl_fc, sa.road_name_field))
    assert expected == actual

def test_get_streetlight_count():
    expected = '849'
    actual = str(sa.get_streetlight_count('CARLING AVE', 0.0002))
    assert expected == actual

def test_save_streetlights():
    import arcpy
    test_fc = r'..\output\RiversideLights.shp'
    sa.save_streetlights('RIVERSIDE DR', 0.0002, test_fc)
    arcpy.env.workspace = r'..\output'
    arcpy.env.overwriteOutput = True
    assert arcpy.Exists('RiversideLights.shp') == True
    arcpy.management.Delete('RiversideLights.shp')
    
    
    