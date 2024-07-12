from python_ushcn.utils.process_data import WeatherData


def test_weatherdata():
    line = "USH0001108411893  1263EX3  1995EX3  2064EX3 -9999 X3 -9999 X3 -9999 X3  3508EX3  3280EX3  3152EX3 -9999 X3  2072EX3  1989EX3"

    wd = WeatherData.from_line(line)

    assert wd.country_code == "US"
    assert wd.network_code == "H"
    assert wd.observer_id == "000110841"
    assert wd.year == 1893

    assert len(wd.values) == 12
    measurement = wd.values[0]
    assert measurement.value == 12.63
    assert measurement.dm_flag == "E"
    assert measurement.qc_flag == "X"
    assert measurement.ds_flag == "3"
