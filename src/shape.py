from shapely.geometry import LineString, Point


line = LineString([(0, 0), (1, 1)])
point = Point(0, 0.5)

distance = line.project(point)

print(distance)