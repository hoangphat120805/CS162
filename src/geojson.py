import json

POINT_PATH = "src/geojson/points.geojson"
LINE_PATH = "src/geojson/lines.geojson"

class GeoJson:
    def __init__(self):
        self.lines = {
            "type": "FeatureCollection",
            "features": []
        }
        self.points = {
            "type": "FeatureCollection",
            "features": []
        }

    def create_point(self, lat, lng, RouteId, RouteVarId, i):
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lng, lat]
            },
            "properties": {
                "RouteId": RouteId,
                "RouteVarId": RouteVarId,
                "index": i
            }
        }
        return feature
        
    def create_line(self, lat1, lng1, lat2, lng2, RouteId, RouteVarId):
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [[lng1, lat1], [lng2, lat2]]
            },
            "properties": {
                "RouteId": RouteId,
                "RouteVarId": RouteVarId
            }
        }
        return feature
        
    def create_points(self, data):
        lat = data.Lat
        lng = data.Lng
        RouteId = data.route_id
        RouteVarId = data.route_var_id
        for i in range(len(lat)):
            self.points["features"].append(self.create_point(lat[i], lng[i], RouteId, RouteVarId, i))

    def create_lines(self, data):
        lat = data.Lat
        lng = data.Lng
        RouteId = data.route_id
        RouteVarId = data.route_var_id
        for i in range(len(lat) - 1):
            self.lines["features"].append(self.create_line(lat[i], lng[i], lat[i+1], lng[i+1], RouteId, RouteVarId))
            
    def output(self):
        with open(POINT_PATH, "w") as f:
            json.dump(self.points, f)
        with open(LINE_PATH, "w") as f:
            json.dump(self.lines, f)

from process_file import read_file
from path import Path, PathQuery
if __name__ == "__main__":
    raw_data = read_file("src/data/paths.json")
    paths = [Path(path) for path in raw_data]
    path_query = PathQuery(paths)
    geojson = GeoJson()
    for path in paths:
        geojson.create_lines(path)
        geojson.create_points(path)
    geojson.output()

