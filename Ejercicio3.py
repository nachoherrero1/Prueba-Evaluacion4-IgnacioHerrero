import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = {}
        self.edges[from_node][to_node] = weight
        if to_node not in self.edges:
            self.edges[to_node] = {}
        self.edges[to_node][from_node] = weight  # As the graph is undirected

    def dijkstra(self, start, end):
        distances = {node: float('infinity') for node in self.nodes}
        previous_nodes = {node: None for node in self.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node == end:
                path = self._build_path(previous_nodes, start, end)
                return distances[end], path
            
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return float("infinity"), []

    def _build_path(self, previous_nodes, start, end):
        path = []
        current_node = end
        while current_node:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        return path

def create_graph():
    graph = Graph()
    graph.add_node("Rivendell")
    graph.add_node("Minas Tirith")
    graph.add_node("Moria")
    graph.add_node("Helm's Deep")
    graph.add_edge("Rivendell", "Moria", 7)
    graph.add_edge("Moria", "Helm's Deep", 5)
    graph.add_edge("Helm's Deep", "Minas Tirith", 11)
    graph.add_edge("Rivendell", "Helm's Deep", 15)
    return graph

def find_shortest_path(graph):
    while True:
        start_city = input("Enter the starting city: ")
        if start_city not in graph.nodes:
            print("City not found in the network.")
            continue
        end_city = input("Enter the destination city: ")
        if end_city not in graph.nodes:
            print("City not found in the network.")
            continue
        
        distance, path = graph.dijkstra(start_city, end_city)
        if distance == float('infinity'):
            print("No path exists between the two cities.")
        else:
            print(f"The shortest path from {start_city} to {end_city} is {distance} units long.")
            print("Path:", " -> ".join(path))
        
        if input("Would you like to find another path? (yes/no): ").lower() != 'yes':
            break

# Create the graph
graph = create_graph()
# Find shortest paths
find_shortest_path(graph)