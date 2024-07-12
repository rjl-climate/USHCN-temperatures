'''
Parse the USHCN station inventory file and create a dictionary of station information.
'''

import os


def parse_stations():
    print("Parsing stations...")
    project_root = os.path.dirname(os.path.dirname(__file__))
    station_file = project_root + "/data/ushcn-stations.txt"
    stations = {}
    with open(station_file) as f:
        for line in f:
            station_code = line[0:11]
            country_code = line[0:1]
            network_code = line[2]
            id_placeholder = line[3:4]
            coop_id = line[5:11]
            lat = float(line[12:20])
            lon = float(line[21:30])
            elevation = float(line[31:37])
            state = line[38:40]
            name = line[41:71]
            component_1 = line[72:78]
            component_2 = line[79:85]
            component_3 = line[86:92]

            stations[station_code] = {
                "station_code": station_code,
                "country_code": country_code,
                "network_code": network_code,
                "id_placeholder": id_placeholder,
                "coop_id": coop_id,
                "lat": lat,
                "lon": lon,
                "elevation": elevation,
                "state": state,
                "name": name,
                "component_1": component_1,
                "component_2": component_2,
                "component_3": component_3,

            }
    return stations


if __name__ == '__main__':
    stations = parse_stations()
    print("Found", len(stations), "stations.")
    print(stations["USH00011084"])
