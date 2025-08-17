from heapq import heappush, heappop
import heapq


class CityGraph:
    def __init__(self):
        self.routes = {}

    def add_route(self, stop1, stop2, distance):
        if stop1 not in self.routes:
            self.routes[stop1] = []
        if stop2 not in self.routes:
            self.routes[stop2] = []

        if (stop2, distance) not in self.routes[stop1]:
            self.routes[stop1].append((stop2, distance))
        if (stop1, distance) not in self.routes[stop2]:
            self.routes[stop2].append((stop1, distance))

    def view_routes(self):
        print("\n📍 City Bus Routes:")
        for stop, connections in self.routes.items():
            connections_str = ", ".join([f"{conn[0]} ({conn[1]} km)" for conn in connections])
            print(f"  {stop} → {connections_str}")

    def find_shortest_route(self, start, end):
        if start not in self.routes or end not in self.routes:
            print("One or both stops are not found.")
            return None, None

        # Dijkstra initialization
        dist = {stop: float('inf') for stop in self.routes}
        prev = {stop: None for stop in self.routes}

        heap = []
        dist[start] = 0
        heappush(heap, (0, start))

        while heap:
            curr_distance, u = heappop(heap)
            # Skip if we already found a shorter path to u
            if curr_distance > dist[u]:
                continue

            for neighbor, weight in self.routes[u]:
                distance = curr_distance + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = u
                    heappush(heap, (distance, neighbor))

        # If no path exists
        if dist[end] == float('inf'):
            print("No route found.")
            return None, None

        # Reconstruct path
        path = []
        curr = end
        while curr is not None:
            path.append(curr)
            curr = prev[curr]
        path.reverse()

        # Print and return
        print(f"Shortest Path: {' -> '.join(path)}")
        print(f"Total Distance: {dist[end]} km")
        return path, dist[end]

    def display_routes(self):
        for stop, connections in self.routes.items():
            routes_str = ", ".join([f"{loc} ({dist} km)" for loc, dist in connections])
            print(f"📍 {stop} -> {routes_str}")








