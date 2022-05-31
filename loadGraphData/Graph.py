
#  adjecency list implementation in python 
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
                self.graph[edge.right].append(edge.left)
        elif edge.right not in self.graph:
            self.graph[edge.right] =[edge.left]
            self.vertices.append(edge.right)

        if edge.left in self.graph:
            if edge.right not in self.graph[edge.left]:
                self.graph[edge.left].append(edge.right)
        elif edge.left not in self.graph:
            self.graph[edge.left] =[edge.right]
            self.vertices.append(edge.left)
        self.edges.append(edge)
       
    def addNode (self,node):
        self.vertices.append(node)

    def print_graph(self):
        for node in self.graph:
            print(node, " --> ",
             [adj_node.value for adj_node in self.graph[node]])
            
    def retNode(self):
        for node in self.vertices:
            print(node,end= ' ')

    def retEdge(self):
        for edge in self.graph:
            print(edge,end= ' ')
