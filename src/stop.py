import json

class Stop:
    def __init__(self, stop):
        for key in stop:
            setattr(self, key, stop[key])
        
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
    def lng(self):
        return self.Lng
    @lng.setter
    def lng(self, value):
        self.Lng = value

    @property
    def lat(self):
        return self.Lat
    @lat.setter
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
    def __init__(self, PATH):
        with open(PATH, 'r', encoding='utf-8') as file:
            file_data = file.read()
        file_parts = file_data.split('}\n{')
        data = json.loads('[' + '},{'.join(file_parts) + ']')
        self.stops = [Stop(stop) for item in data for stop in item['Stops']]
           
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
        return [stop for stop in self.stops for route in stop.routes if route == routes]
    

