
# python implementation of breadth first search
import create_Graph as CG

def breadthFirst( graph , node,destin):
    visited = []
    queue = [node]

    while queue:
        tempNode = queue.pop(0)

        for neighbhour in graph[tempNode]:
            if neighbhour not in visited:
                queue.append(neighbhour)

        if tempNode not in visited:
            visited.append(tempNode)

            if tempNode == destin:
                path = []
                for node in visited: 
                    path.append(node.value)
                return path



graph = CG.createGraph('city_data.txt')
node = graph.vertices[0]
node2 = graph.vertices[5]
print(breadthFirst(graph.graph,node,node2))