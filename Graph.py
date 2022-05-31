
#  adjecency list to implement graph in python 
class Node :
    def __init__(self,value):
        self.value = value
    def __str__(self) :
        return str(self.value)
    
class Edge:
    def __init__(self,left ,right ,weight = 1) :
        self.left = left
        self.right = right
        self.weight = weight

class Graph : 
    def __init__(self) :
        self.vertices = []
        self.edges = []
        self.graph = {}
        
    def addEdge(self,edge):
        if edge.right in self.graph:
            if edge.left not in self.graph[edge.right]:
                self.graph[edge.right][edge.left] = edge.weight
        elif edge.right not in self.graph:
            self.graph[edge.right] ={edge.left:edge.weight}
            self.vertices.append(edge.right)

        if edge.left in self.graph:
            if edge.right not in self.graph[edge.left]:
                self.graph[edge.left][edge.right] = edge.weight
        elif edge.left not in self.graph:
            self.graph[edge.left] ={edge.right:edge.weight}
            self.vertices.append(edge.left)
        self.edges.append(edge)
       
    def addNode (self,node):
        self.vertices.append(node)

    def print_graph(self):
        for node in self.graph:
            print(node, " --> ",
             {adj_node.value:self.graph[node][adj_node]
              for adj_node in self.graph[node]})
            
   
    def retNode(self):
        for node in self.vertices:
            print(node,end= ' ')

    def retEdge(self):
        for edge in self.graph:
            print(edge,end= ' ')



# this function reads data from file and create a graph
def createGraph(data):
    graph = Graph()                
    visited = []
    node_list = []
    temp_node = []
    weight = 1
    with open(data,'r') as file: 
        for line in file:
            for word in line.split():
                if word.isdigit():
                    weight = word
                if word.isalpha():
                    if word in visited:
                        for node in node_list:
                            if node.value == word:
                                temp_node.append(node)
                    else:
                        node = Node(word)
                        temp_node.append(node)
                        node_list.append(node)
                        visited.append(word)
            
            node1 = temp_node.pop(0)
            node2 = temp_node.pop(-1)
            edge = Edge(node1,node2,weight)
            graph.addEdge(edge)   
        return graph

   
    
graph = createGraph('city_data.txt')
# graph.print_graph()
# for edge in graph.edges:
#     print(edge.right.value, edge.left.value , edge.weight)

# Oradea = Node("Oradea")
# Zerid = Node("Zerid")
# Arad = Node("Arad")
# Sibiu = Node("Sibiu")
# Fagaras = Node("Fagaras")
# Timisoara = Node("Timisoara")
# Rimnicu = Node("Rimnicu_Vilcea")
# Mehadia = Node("Mehadia")
# Drobeta = Node("Drobeta")
# Pitesti = Node("Pitesti")
# Craiova = Node("Craiova")
# Lugoj = Node("Lugoj")
# Giurgiu = Node("Giurgiu")
# Bucharest = Node("Bucharest")
# Urziceni = Node("Urziceni")
# eforie = Node("Eforie")
# Hirsova = Node("Hirsova")
# Valslui = Node("Valslui")
# Iasi = Node("Iasi")
# Neamt = Node("Neamt")


# edge_A = Edge(Oradea,Zerid,71)
# edge_B = Edge(Arad,Zerid,75)
# edge_C = Edge(Oradea,Sibiu,151)
# edge_D = Edge(Arad,Sibiu,140)
# edge_E = Edge(Arad,Timisoara,118)
# edge_F = Edge(Timisoara,Lugoj,111)
# edge_G = Edge(Lugoj,Mehadia,70)
# edge_H = Edge(Mehadia,Drobeta,75)
# edge_I = Edge(Drobeta,Craiova,120)
# edge_J = Edge(Sibiu,Rimnicu,80)
# edge_K = Edge(Rimnicu,Pitesti,97)
# edge_L = Edge(Rimnicu,Craiova,146)
# edge_M = Edge(Sibiu,Fagaras,99)
# edge_N = Edge(Fagaras,Bucharest,211)
# edge_O = Edge(Pitesti,Bucharest,101)
# edge_P = Edge(Bucharest,Giurgiu,90)
# edge_Q = Edge(Bucharest,Urziceni,85)
# edge_R = Edge(Urziceni,Hirsova,98)
# edge_S = Edge(Hirsova,eforie,86)
# edge_T = Edge(Urziceni,Valslui,142)
# edge_U = Edge(Valslui,Iasi,92)
# edge_V = Edge(Iasi,Neamt,87)


# edge_List = [edge_A, edge_B, edge_C, edge_D, edge_E, edge_F, edge_G,edge_H,
#              edge_I, edge_J, edge_K, edge_L, edge_M, edge_N, edge_N, edge_O,
#              edge_P, edge_Q, edge_R, edge_S, edge_T, edge_U, edge_V]


# for edge in edge_List:
#     graph.addEdge(edge)

