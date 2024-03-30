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
    
    

class RouteVarQuery:
    def __init__
