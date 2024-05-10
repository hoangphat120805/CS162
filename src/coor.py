from pyproj import Proj, Transformer

proj_source = Proj('epsg:4326')
proj_dest = Proj('epsg:3405')
transformer = Transformer.from_crs('epsg:4326', 'epsg:3405')
def convert_coordinate(lat, lng):
    x, y = [0.0, 0.0]
    x, y = transformer.transform(lat, lng)
    return x, y
    