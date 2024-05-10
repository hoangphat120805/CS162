from typing import Any
from coor import convert_coordinate
from process_file import read_file
import heapq
from shapely import LineString, Point
import json
import time

class Data:
    def __init__(self, start_stop, end_stop, time):
        self.start_stop = start_stop
        self.end_stop = end_stop
        self.time = time

class ShortestPath:
    def __init__(self, start_stop, end_stop, time, path, stop_path_query):
        self.start_stop = start_stop
        self.end_stop = end_stop
        self.time = time
        self.path = path
        self.stops = []
        last_u = 0
        last_r = 0
        last_rv = 0
        for u, r, rv in path:
            if u == last_u and r == last_r and rv == last_rv:
                continue
            ans = stop_path_query.searchStopPath(route_id=str(r), route_var_id=str(rv))
            for stop_path in ans:
                self.stops.append(stop_path.__dict__)

class Graph:
    def __init__(self, route_var_query, stop_path_query, path_query, stop_query):
        self.edge = []
        self.cnt = [[0, i] for i in range(8000)]
        self.route_var_query = route_var_query
        self.stop_path_query = stop_path_query
        self.path_query = path_query
        self.stop_query = stop_query
        for i in range(8000):
            self.edge.append([])
        self.build()

    def build(self):
        for route in self.route_var_query.routes:
            stops_path = self.stop_path_query.searchStopPath(route_id=route.route_id_str, route_var_id=route.route_var_id_str)
            path = self.path_query.searchPath(route_id=route.route_id_str, route_var_id=route.route_var_id_str)
            self.add_edge(route, stops_path[0], path[0])

    def add_edge(self, route, stops_path, path):
        line = LineString([convert_coordinate(path.latitude[i], path.longitude[i]) for i in range(len(path.latitude))])
        
        for i in range(len(stops_path.stops)):
            if i == len(stops_path.stops) - 1:
                break
            lat = stops_path.stops[i].latitude
            lng = stops_path.stops[i].longitude
            x, y = convert_coordinate(lat, lng)
            lat2 = stops_path.stops[i+1].latitude
            lng2 = stops_path.stops[i+1].longitude
            x2, y2 = convert_coordinate(lat2, lng2)
            point1 = Point(x, y)
            point2 = Point(x2, y2)
            distance = abs(line.project(point1) - line.project(point2))
            self.edge[stops_path.stops[i].stop_id].append((stops_path.stops[i+1].stop_id, route.running_time/route.distance*distance, distance, route.route_id, route.route_var_id))
        

    def shortest_path(self, start, end):
        n = 8000
        last = [(0, 0)] * n
        time = [1e9] * n
        time[start] = 0
        pq = []
        heapq.heappush(pq, (0, start, 0, 0))
        while len(pq) > 0:
            d, u, r, rv = heapq.heappop(pq)
            if d > time[u]:
                continue
            if u == end:
                break
            for v, t, di, r, rv in self.edge[u]:
                if time[v] > d + t:
                    time[v] = d + t
                    heapq.heappush(pq, [time[v], v, r, rv])
                    last[v] = (u, r, rv)
                
        path = []
        if time[end] == 1e9:
            return path, -1
        
        u = end
        r = 0
        rv = 0
        while u != start:
            path.append((u, r, rv))
            u, r, rv = last[u]
        path.append((start, r, rv))
        path.reverse()
        return [ShortestPath(start, end, time[end], path, self.stop_path_query)]
    
    def dijkstra_n(self, start):
        n = 8000
        ti = [1e9] * n
        ti[start] = 0
        pq = []
        heapq.heappush(pq, (0, start))
        while len(pq) > 0:
            d, u = heapq.heappop(pq)

            if d > ti[u]:
                continue

            for v, t, di, r, rv in self.edge[u]:
                if ti[v] > d + t:
                    ti[v] = d + t
                    heapq.heappush(pq, (ti[v], v))
        return ti

    def all_shortest_path(self):
        n = 8000
        all_path = []
        t = time.time()
        for stop in self.stop_query.stops:
            print(time.time()-t)
            ti = self.dijkstra_n(stop.stop_id)
            for i in range(n):
                if ti[i] == 1e9:
                    continue
                di = Data(stop.stop_id, i, ti[i])
                all_path.append(di) 
            print ("\033[A                             \033[A")
        print(time.time()-t)
        return all_path
    
    def dijkstra_trace(self, start):
        n = 8000
        ti = [1e9] * n
        trace = [(-1, 0)] * n
        ti[start] = 0
        pq = []
        heapq.heappush(pq, (0, start, 0))
        while len(pq) > 0:
            d, u, h = heapq.heappop(pq)

            if d > ti[u]:
                continue

            for v, t, di, r, rv in self.edge[u]:
                if ti[v] > d + t:
                    ti[v] = d + t
                    heapq.heappush(pq, (ti[v], v, h+1))
                    trace[v] = (u, h+1)
        cnt = [0]*n
        for i in range(n):
            if trace[i][0] == -1:
                continue
            heapq.heappush(pq, (-trace[i][1], i))
            cnt[i] = 1
        while len(pq) > 0:
            h, u = heapq.heappop(pq)
            if cnt[u] == 0:
                continue

            if trace[u][0] != -1:
                cnt[trace[u][0]] += cnt[u]
                heapq.heappush(pq, (-trace[u][1], trace[u][0]))
            
            self.cnt[u][0] += cnt[u]
            cnt[u] = 0
        
    
    def k_importance_stops(self, k):
        if self.cnt[0][0] == 0:
            t = time.time()
            for stop in self.stop_query.stops:
                print(time.time()-t)
                self.dijkstra_trace(stop.stop_id)
                print ("\033[A                             \033[A")
            self.cnt.sort(key=lambda x: x[0], reverse=True)
            print(time.time()-t)
        ans = []
        for i in range(k):
            stops = self.stop_query.searchStop(stop_id=self.cnt[i][1])
            for stop in stops:
                ans.append(stop)
        return ans
    
    def floyd_warshall(self):
        n = 8000
        dist = [[1e9]*n for i in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for i in range(n):
            for v, t, di, r, rv in self.edge[i]:
                dist[i][v] = t
        t = time.time()
        for k in range(n):
            if self.edge[k] == []:
                continue
            for i in range(n):
                if self.edge[i] == []:
                    continue
                for j in range(n):
                    print(time.time()-t)
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    print ("\033[A                             \033[A")
        print(time.time()-t)
        return dist
    
    