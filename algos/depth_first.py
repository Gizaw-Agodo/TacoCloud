import create_Graph as CG

def depthFirst(graph,node,destin):
    stack = [node]
    visited = []

    while len(stack) != 0:
        node1 = stack.pop()

        if node1 not in  visited : 
            visited.append(node1)
            if node1 == destin:
                return [visited.value for visited in visited]
        
        for node in graph[node1]:
            if node not in visited:
                stack.append(node)
    return None

graph = CG.createGraph('city_data.txt')
node = graph.vertices[0]
depthFirst(graph.graph,node,node)