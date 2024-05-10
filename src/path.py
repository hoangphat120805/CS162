import json
class Path:
    def __init__(self, path):
        for key, value in path.items():
            setattr(self, key, value)
    
    @property
    def latitude(self):
        return self.lat
    @latitude.setter
    def Lat(self, value):
        self.lat = value

    @property
    def longitude(self):
        return self.lng
    @longitude.setter
    def Lng(self, value):
        self.lng = value

    @property
    def route_id(self):
        return self.RouteId
    @route_id.setter
    def route_id(self, value):
        self.RouteId = value

    @property
    def route_var_id(self):
        return self.RouteVarId
    @route_var_id.setter
    def route_var_id(self, value):
        self.RouteVarId = value

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
    
    def __repr__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class PathQuery:
    def __init__(self, raw_paths):
        self.paths = [Path(path) for path in raw_paths]
    
    def searchByRouteId(self, route_id):
        return [path for path in self.paths if path.route_id == route_id]
    
    def searchByRouteVarId(self, route_var_id):
        return [path for path in self.paths if path.route_var_id == route_var_id]
    
    def searchByRouteIdAndRouteVarId(self, route_id, route_var_id):
        return [path for path in self.paths if path.route_id == route_id and path.route_var_id == route_var_id]

    def searchPath(self, **kwargs):
        return [path for path in self.paths if all(getattr(path, key) == value for key, value in kwargs.items())]


