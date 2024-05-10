# {"StopId":35,"Code":"BX 01","Name":"Bến xe buýt Sài Gòn","StopType":"Bến xe","Zone":"Quận 1","Ward":"Phường Phạm Ngũ Lão","AddressNo":"BẾN XE BUÝT SÀI GÒN","Street":"Lê Lai","SupportDisability":"Có","Status":"Đang khai thác","Lng":106.689362,"Lat":10.767676,"Search":"BxbSG BXBSG LL","Routes":"03, 04, 102, 109, 120, 13, 140, 18, 19, 20, 27, 28, 34, 36, 39, 52, 61-6, 65, 69, 70-3, 72, 75, 86, 88, 93, D1"}

class Stop:
    def __init__(self, stops):
        for key in stops:
            setattr(self, key, stops[key])
    @property
    def stop_id(self):
        return self.StopId
    @stop_id.setter
    def stop_id(self, value):
        self.StopId = value

    @property
    def code(self):
        return self.Code
    @code.setter
    def code(self, value):
        self.Code = value

    @property
    def name(self):
        return self.Name
    @name.setter
    def name(self, value):
        self.Name = value

    @property
    def stop_type(self):
        return self.StopType
    @stop_type.setter
    def stop_type(self, value):
        self.StopType = value

    @property
    def zone(self):
        return self.Zone
    @zone.setter
    def zone(self, value):
        self.Zone = value

    @property
    def ward(self):
        return self.Ward
    @ward.setter
    def ward(self, value):
        self.Ward = value

    @property
    def address_no(self):
        return self.AddressNo
    @address_no.setter
    def address_no(self, value):
        self.AddressNo = value

    @property
    def street(self):
        return self.Street
    @street.setter
    def street(self, value):
        self.Street = value

    @property
    def support_disability(self):
        return self.SupportDisability
    @support_disability.setter
    def support_disability(self, value):
        self.SupportDisability = value

    @property
    def status(self):
        return self.Status
    @status.setter
    def status(self, value):
        self.Status = value

    @property
    def longitude(self):
        return self.Lng
    @longitude.setter
    def lng(self, value):
        self.Lng = value

    @property
    def latitude(self):
        return self.Lat
    @latitude.setter
    def lat(self, value):
        self.Lat = value

    @property
    def search(self):
        return self.Search
    @search.setter
    def search(self, value):
        self.Search = value

    @property
    def routes(self):
        return self.Routes
    @routes.setter
    def routes(self, value):
        self.Routes = value

class StopQuery: 
    def __init__(self, raw_stops):
        self.stops = []
        for stops in raw_stops:
            for stop in stops["Stops"]:
                if any(stop["StopId"] == tmp.stop_id for tmp in self.stops) == False:
                    self.stops.append(Stop(stop))
        self.stops.sort(key=lambda x: x.stop_id)

    def searchByStopId(self, stop_id):
        return [stop for stop in self.stops if stop.stop_id == stop_id]
    
    def searchByCode(self, code):
        return [stop for stop in self.stops if stop.code == code]
    
    def searchByName(self, name):
        return [stop for stop in self.stops if stop.name == name]
    
    def searchByStopType(self, stop_type):
        return [stop for stop in self.stops if stop.stop_type == stop_type]
    
    def searchByZone(self, zone):
        return [stop for stop in self.stops if stop.zone == zone]
    
    def searchByWard(self, ward):
        return [stop for stop in self.stops if stop.ward == ward]
    
    def searchByAddressNo(self, address_no):
        return [stop for stop in self.stops if stop.address_no == address_no]
    
    def searchByStreet(self, street):
        return [stop for stop in self.stops if stop.street == street]
    
    def searchBySupportDisability(self, support_disability):
        return [stop for stop in self.stops if stop.support_disability == support_disability]
    
    def searchByStatus(self, status):
        return [stop for stop in self.stops if stop.status == status]
    
    def searchByLng(self, lng):
        return [stop for stop in self.stops if stop.lng == lng]
    
    def searchByLat(self, lat):
        return [stop for stop in self.stops if stop.lat == lat]
    
    def searchBySearch(self, search):
        return [stop for stop in self.stops if stop.search == search]
    
    def searchByRoutes(self, routes):
        return [stop for stop in self.stops if stop.routes == routes]
    
    def searchStop(self, **kwargs):
        return [stop for stop in self.stops if all(getattr(stop, key) == value for key, value in kwargs.items())]

class StopPath:
    def __init__(self, data):
        stops = []
        for stop in data["Stops"]:
            stops.append(Stop(stop))
        self.Stops = stops
        self.RouteId = data["RouteId"]
        self.RouteVarId = data["RouteVarId"]

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
    def stops(self):
        return self.Stops
    @stops.setter
    def stops(self, value):
        self.Stops = value

    @property
    def __dict__(self):
        return {
            "RouteId": self.RouteId,
            "RouteVarId": self.RouteVarId,
            "Stops": [stop.__dict__ for stop in self.Stops]
        }
    

class StopPathQuery:
    def __init__(self, raw_stops):
        self.stop_paths = []
        for stop_path in raw_stops:
            self.stop_paths.append(StopPath(stop_path))
        
    def searchByRouteId(self, route_id):
        return [stop_path for stop_path in self.stop_paths if stop_path.route_id == route_id]
    
    def searchByRouteVarId(self, route_var_id):
        return [stop_path for stop_path in self.stop_paths if stop_path.route_var_id == route_var_id]
    
    def searchByRouteIdAndRouteVarId(self, route_id, route_var_id):
        return [stop_path for stop_path in self.stop_paths if stop_path.route_id == route_id and stop_path.route_var_id == route_var_id]
    
    def searchStopPath(self, **kwargs):
        return [stop_path for stop_path in self.stop_paths if all(getattr(stop_path, key) == value for key, value in kwargs.items())]
