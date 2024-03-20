import json
from route_var import RouteVar 
from route_var import RouteVarQuery

VARS_PATH = "src/vars.json"

# Tạo đối tượng RouteVarQuery
ans = RouteVarQuery(VARS_PATH).searchByRouteId(1, 3)
print(json.dumps(ans, default=lambda o: o.__dict__, indent=4, ensure_ascii=False))

