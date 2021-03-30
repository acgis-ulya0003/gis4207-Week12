import streetlight_analyzer as sa

sa.roads_cl_fc = r'..\..\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'


def test_get_unique_values():

    expected = 'MITCH OWENS RD'
    actual = list(sa._get_unique_values(sa.roads_cl_fc, road_name_field))[0]
    assert expected == actual