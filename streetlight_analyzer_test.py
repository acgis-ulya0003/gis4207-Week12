import streetlight_analyzer as sa

sa.roads_cl_fc = r'..\..\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
sa.road_name_field = 'ROAD_NAME_'

def test_get_unique_values():

    expected = 8674
    actual = len(sa._get_unique_values(sa.roads_cl_fc, sa.road_name_field))
    assert expected == actual