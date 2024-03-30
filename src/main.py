import json
from route_var import RouteVar 
from route_var import RouteVarQuery
from stop import Stop
from stop import StopQuery

VARS_PATH = "src/data/vars.json"
STOPS_PATH = "src/data/stops.json"

# Tạo đối tượng RouteVarQuery
ans = RouteVarQuery(VARS_PATH).searchByRouteVarId(1, 1)
print(ans.outputASJson())

# Tạo đối tượng StopQuery
# ans1 = StopQuery(STOPS_PATH).searchByStopId(1)
# print(json.dumps(ans1, default=lambda o: o.__dict__, separators=(",")))

