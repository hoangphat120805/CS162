from process_file import read_file, outputAsJson, outputAsCSV
from geojson import GeoJson
from route_var import RouteVar, RouteVarQuery
from stop import Stop, StopQuery, StopPathQuery, StopPath, StopPathQuery
from path import Path, PathQuery
from graph import Graph
from test_ai import test_ai
import json
import time


VARS_PATH = "src/data/vars.json"
STOPS_PATH = "src/data/stops.json"
PATHS_PATH = "src/data/paths.json"

VARS_OUTPUT_PATH = "src/output/vars"
STOPS_OUTPUT_PATH = "src/output/stops"
PATHS_OUTPUT_PATH = "src/output/paths"


def main():
    raw_vars = read_file(VARS_PATH)
    raw_stops = read_file(STOPS_PATH)
    raw_paths = read_file(PATHS_PATH)
    route_var_query = RouteVarQuery(raw_vars)
    stop_query = StopQuery(raw_stops)
    path_query = PathQuery(raw_paths)
    stop_path_query = StopPathQuery(raw_stops)
    graph = Graph(route_var_query, stop_path_query, path_query, stop_query)
    test_ai(route_var_query, stop_query, path_query, graph)



    



if __name__ == "__main__":
    main()
    

