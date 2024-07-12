from python_ushcn.daily.stations import Station


def test_stations():
    line = "USS0010J18S  40.5500 -110.6900 2404.6 UT Rock Creek"

    s = Station.from_line(line)

    assert s.id == "USS0010J18S"
    assert s.latitude == 40.55
    assert s.longitude == -110.69
    assert s.elevation == 2404.6
    assert s.state == "UT"
    assert s.name == "Rock Creek"
