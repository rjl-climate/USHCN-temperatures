from python_ushcn.daily.deserialise import WeatherData


def test_daily_weatherdata():
    line = "USC00011084192601TMAX-9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999   -9999     239  6  222  6   50  6   50  6  144  6  144  6  161  6  144  6  150  6  128  6  200  6"

    wd = WeatherData.from_line(line)

    assert wd.id == "USC00011084"
    assert wd.year == 1926
    assert wd.month == 1
    assert wd.element == "TMAX"

    assert len(wd.values) == 31
    assert wd.values[0].value is None
    assert wd.values[29].value == 1.28
