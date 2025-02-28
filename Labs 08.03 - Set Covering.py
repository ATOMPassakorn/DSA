def findStations(city,stations):
    cover_city = set(city)
    selected_stations = []
    stations_list = []
    while cover_city:
        best_station = None
        best_cover = 0
        for station in stations:
            covered_cities = set(station['Cities'])
            cover_count = len(cover_city & covered_cities)
            if cover_count > best_cover:
                best_cover = cover_count
                best_station = station
        if best_station:
            selected_stations.append(best_station)
            cover_city -= set(best_station['Cities'])
            stations.remove(best_station)
        else:
            break
    for station in selected_stations:
        stations_list.append(station["Name"])
    stations_list.sort()
    print(stations_list)
import json
def main():
    city = json.loads(input())
    radio_num = int(input())
    stations = []
    for _ in range(radio_num):
        station_in = json.loads(input())
        stations.append(station_in)
    findStations(city,stations)
main()