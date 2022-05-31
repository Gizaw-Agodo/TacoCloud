import Graph as G
# this function reads data from file and create a graph
def createGraph(data):
    graph = G.Graph()                
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
                        node = G.Node(word)
                        temp_node.append(node)
                        node_list.append(node)
                        visited.append(word)
            
            node1 = temp_node.pop(0)
            node2 = temp_node.pop(-1)
            edge = G.Edge(node1,node2,weight)
            graph.addEdge(edge)   
    return graph    
    
graph = createGraph('city_data.txt')
graph.print_graph()
