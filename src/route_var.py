import json
class RouteVar:
    def __init__(self, Route):
        for key in Route:
            setattr(self, key, Route[key])
        
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

    @property
    def route_var_name(self):
        return self.RouteVarName
    @route_var_name.setter
    def route_var_name(self, value):
        self.RouteVarName = value

    @property
    def route_var_short_name(self):
        return self.RouteVarShortName
    @route_var_short_name.setter
    def route_var_short_name(self, value):
        self.RouteVarShortName = value

    @property
    def route_no(self):
        return self.RouteNo
    @route_no.setter
    def route_no(self, value):
        self.RouteNo = value

    @property
    def start_stop(self):
        return self.StartStop
    @start_stop.setter
    def start_stop(self, value):
        self.StartStop = value

    @property
    def end_stop(self):
        return self.EndStop
    @end_stop.setter
    def end_stop(self, value):
        self.EndStop = value

    @property
    def distance(self):
        return self.Distance
    @distance.setter
    def distance(self, value):
        self.Distance = value

    @property
    def outbound(self):
        return self.Outbound
    @outbound.setter
    def outbound(self, value):
        self.Outbound = value

    @property
    def running_time(self):
        return self.RunningTime
    @running_time.setter
    def running_time(self, value):
        self.RunningTime = value

    @property
    def route_id_str(self):
        return str(self.route_id)

    @property
    def route_var_id_str(self):
        return str(self.route_var_id)


    
class RouteVarQuery:
    def __init__(self, raw_vars):
        self.routes = [RouteVar(var) for route in raw_vars if len(route) > 0 for var in route]  
    
    def searchByRouteId(self, route_id: int):
        return [route for route in self.routes if route.route_id == route_id]
    
    def searchByRouteVarId(self, route_var_id):
        return [route for route in self.routes if route.route_var_id == route_var_id]
    
    def searchByRouteVarName(self, name):
        return [route for route in self.routes if route.route_var_name == name]
    
    def searchByRouteVarShortName(self, name):
        return [route for route in self.routes if route.route_var_short_name == name]
    
    def searchByRouteNo(self, no):
        return [route for route in self.routes if route.route_no == no]
    
    def searchByStartStop(self, name):
        return [route for route in self.routes if route.start_stop == name]
    
    def searchByEndStop(self, name):
        return [route for route in self.routes if route.end_stop == name]
    
    def searchByDistance(self, distance):
        return [route for route in self.routes if route.distance == distance]
    
    def searchByOutbound(self, name):
        return [route for route in self.routes if route.outbound == name]
    
    def searchByRunningTime(self, running_time):
        return [route for route in self.routes if route.running_time == running_time]

    def searchRoute(self, **kwargs):
        return [route for route in self.routes if all(getattr(route, key) == value for key, value in kwargs.items())]
