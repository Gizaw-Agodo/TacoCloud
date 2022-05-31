
class Node:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.edge_list = []
        self.incident_nodes = []
        self.latitude = latitude
        self.longitude = longitude
        self.heuristic_distance = None
        self.from_start = float('inf')
        self.f_value = float('inf')


    def connect(self, node):
        con = (self.name, node.name)
        self.edge_list.append(con)

    def join_node(self, node):
        adjacent_node = node.name
        self.incident_nodes.append(adjacent_node)


class Edge:

    def __init__(self, left, right, weight=1):
        self.left = left
        self.right = right
        self.weight = weight


class Graph:

    def __init__(self):
        self.verticies = {}
        self.edges = {}

    def add_node(self, node):
        self.verticies[node.name] = node

    def add_edge(self, left, right, weight=1):
        if left.name not in self.verticies:
            self.verticies[left.name] = left

        if right.name not in self.verticies:
            self.verticies[right.name] = right

        left.incident_nodes.append(right.name)
        right.incident_nodes.append(left.name)

        e = Edge(left, right, weight)

        key = (left.name, right.name)
        self.edges[key] = e

        key = (right.name, left.name)
        self.edges[key] = e

        left.edge_list.append((left.name, right.name))
        left.edge_list.append((right.name, left.name))


    def read_file(self, text_file):
        file = open(text_file, 'r')

        for row in file:
            row = row.split(' ')
            a = Node(row[0], float(row[1]), float(row[2]))
            b = Node(row[3], float(row[4]), float(row[5]))
            for vertex in self.verticies.values():
                if vertex.name == row[0]:
                    a = vertex
                    break
                else:
                    a = Node(row[0], float(row[1]), float(row[2]))

            for vertex in self.verticies.values():
                if vertex.name == row[3]:
                    b = vertex
                    break
                else:
                    b = Node(row[3], float(row[4]), float(row[5]))

            wgt = int(row[6])

            self.add_edge(a, b, weight=wgt)


    def aStarSearch(self, start, destination):
        open_list = []
        closed_list = []
        shortest_path = []
        current = start
        parent_node = {}

        for vertex in self.verticies.values():
            vertex.heuristic_distance = None
            vertex.from_start = float('inf')
            vertex.f_value = float('inf')

        # finding heuristic distance using manhathan distance
        x_coord = abs(start.latitude - destination.latitude)
        y_coord = abs(start.longitude - destination.longitude)

        start.heuristic_value = (x_coord + y_coord)
        start.from_start = 0

        closed_list.append(start)
        while current != destination:
            for node in current.incident_nodes:
                node = self.verticies[node]
                if node not in closed_list:
                    if node not in open_list:
                        open_list.append(node)

                    from_start_cost = current.from_start + self.edges[(node.name, current.name)].weight
                    if from_start_cost < node.from_start:
                        node.from_start = from_start_cost

                    x_coord = abs(node.latitude - destination.latitude)
                    y_coord = abs(node.longitude - destination.longitude)
                    node.heuristic_distance = (x_coord + y_coord)
                    node_cost = node.heuristic_distance + node.from_start

                    if node_cost < node.f_value:
                        node.f_value = node_cost
                        parent_node[node.name] = current

            lowest_value_node = open_list[0]
            for node in open_list:
                if node.f_value < lowest_value_node.f_value:
                    lowest_value_node = node
            current = lowest_value_node
            closed_list.append(current)
            open_list.remove(lowest_value_node)

        last_node = destination
        while last_node.name != start.name:
            shortest_path.insert(0,last_node.name)
            last_node = parent_node[last_node.name]
        shortest_path.insert(0,last_node.name)

        # print(shortest_path)
        return destination.from_start,shortest_path


    def dijkstraAlgorithm(self, start, destination):
        open_list = []
        closed_list = []
        shortest_path = []
        distance = {}
        current = start
        parent_node = {}

        for vertex in self.verticies.values():
            vertex.from_start = float('inf')
            distance[vertex.name] = vertex.from_start

        start.from_start = 0
        distance[start.name] = start.from_start

        while len(closed_list) != len(self.verticies.values()):
            for node in current.incident_nodes:
                node = self.verticies[node]
                if node not in closed_list:
                    if node not in open_list:
                        open_list.append(node)
                    node_cost  = current.from_start + self.edges[(node.name, current.name)].weight

                    if node_cost < node.from_start:
                        node.from_start = node_cost
                        parent_node[node.name] = current
                        distance[node.name] = node.from_start

            lowest_value_node = open_list[0]
            for node in open_list:
                if node.from_start < lowest_value_node.from_start:
                    lowest_value_node = node
            current = lowest_value_node
            closed_list.append(current)
            open_list.remove(lowest_value_node)

        last_node = destination
        while last_node.name != start.name:
            shortest_path.insert(0,last_node.name)
            last_node = parent_node[last_node.name]
        shortest_path.insert(0,last_node.name)

        # print(distance)
        return destination.from_start,shortest_path

    def aStarSearchClosenessCentrality(self):
        closeness_value = {}
        number_of_nodes = len(self.verticies.values())
        for start in self.verticies.values():
            sum = 0
            for destination in self.verticies.values():
                result,b = self.aStarSearch(start, destination)
                sum += result

            # standard closeness centrality formula is (n - 1) / sum
            node_closeness_centrality = (number_of_nodes - 1) / sum
            closeness_value[start.name] = node_closeness_centrality
        print(closeness_value)

    def dijkstraClosenessCentrality(self):
        closeness_value = {}
        number_of_nodes = len(self.verticies.values())
        for start in self.verticies.values():
            sum = 0
            for destination in self.verticies.values():
                result,b =self.dijkstraAlgorithm(start, destination) 
                sum += result

            # standard closeness centrality formula is (n - 1) / sum
            node_closeness_centrality = (number_of_nodes - 1) / sum
            closeness_value[start.name] = node_closeness_centrality
        print(closeness_value)


    def degreeCentrality(self):
        degree_centrality_value = {}
        number_of_nodes = len(self.verticies.values())
        for node in self.verticies.values():
            degree = len(node.edge_list)

            # standard degree centrality is calculated as degree / (n - 1)
            node_degree_centrality = degree / (number_of_nodes - 1)
            degree_centrality_value[node.name] = node_degree_centrality

        maximum = max(degree_centrality_value.values())
        for key, value in degree_centrality_value.items():
            if value == maximum:
                print(key)


    def astarBetweenessCentralit(self):
        vertices = self.verticies.values()
        for vertex in vertices:
            visited = []
            betweens = 0
            for vertex1 in vertices:
                if vertex1 == vertex :
                    continue 
                visited.append(vertex1)
                for vertex2 in vertices:
                    if vertex2 == vertex or vertex2 in visited or vertex2 == vertex1:
                        continue
                    else:
                        result,short_path = self.aStarSearch(vertex1,vertex2)
                        if vertex.name in short_path[1:-1]:
                            calc_betweeness = 1
                            betweens += calc_betweeness
            print(vertex.name,"-->" , betweens)

    
    def djekstraBetweenessCentralit(self):
            vertices = self.verticies.values()
            for vertex in vertices:
                visited = []
                betweens = 0
                for vertex1 in vertices:
                    if vertex1 == vertex :
                        continue 
                    visited.append(vertex1)
                    for vertex2 in vertices:
                        if vertex2 == vertex or vertex2 in visited or vertex2 == vertex1:
                            continue
                        else:
                            result,short_path = self.dijkstraAlgorithm(vertex1,vertex2)
                            if vertex.name in short_path[1:-1]:
                                calc_betweeness = 1
                                betweens += calc_betweeness
                print(vertex.name,'-->', betweens)



g = Graph()

g.read_file("in.txt")
# g.degreeCentrality()
# g.dijkstraClosenessCentrality()
print("++++++++++++++++++++")
# g.aStarSearchClosenessCentrality()
print("-______________")
g.astarBetweenessCentralit()
print("-______________")
# g.djekstraBetweenessCentralit()