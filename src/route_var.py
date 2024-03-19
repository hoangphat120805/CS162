class RouteVar:
    # def __init__(self, RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, Outbound, RunningTime):
    #     self.RouteId = RouteId
    #     self.RouteVarId = RouteVarId
    #     self.RouteVarName = RouteVarName
    #     self.RouteVarShortName = RouteVarShortName
    #     self.RouteNo = RouteNo
    #     self.StartStop = StartStop
    #     self.EndStop = EndStop
    #     self.Distance = Distance
    #     self.Outbound = Outbound
    #     self.RunningTime = RunningTime
    def __init__(self, Route):
        for key, value in Route.items():
            # print(key, value)
            setattr(self, key, value)

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
    
    

class RouteVarQuery(RouteVar):
    def __init__(self, vars):
        self.routeVar = vars
        
    def searchByRouteId(self, mn, mx):
        return [var for var in self.routeVar if mn <= var.route_id <= mx]
    
    def searchByRouteVarId(self, mn, mx):
        return [var for var in self.routeVar if mn <= var.route_var_id <= mx]
    
    def searchByRouteVarName(self, name):
        return [var for var in self.routeVar if name in var.route_var_name]
    
    def searchByRouteVarShortName(self, name):
        return [var for var in self.routeVar if name in var.route_var_short_name]
    
    def searchByRouteNo(self, no):
        return [var for var in self.routeVar if no == var.route_no]
    
    def searchByStartStop(self, name):
        return [var for var in self.routeVar if name in var.start_stop]
    
    def searchByEndStop(self, name):
        return [var for var in self.routeVar if name in var.end_stop]
    
    def searchByDistance(self, mn, mx):
        return [var for var in self.routeVar if mn <= var.distance <= mx]
    
    def searchByOutbound(self, name):
        return [var for var in self.routeVar if name in var.outbound]
    
    def searchByRunningTime(self, mn, mx):
        return [var for var in self.routeVar if mn <= var.running_time <= mx]
    
