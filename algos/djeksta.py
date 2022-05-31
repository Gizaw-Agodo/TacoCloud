
from cmath import inf
import create_Graph as CG

def dijkstra(graph, src):
    distances = {}
    for vertex in graph.vertices :
        distances[vertex] = inf 

    distances[src] = 0
    unvisited = graph.vertices

    while unvisited:
        
        current_vertex = min( unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == inf:
            break

        for neighbour in graph.graph[current_vertex]:
            temp_route = distances[current_vertex] + \
            int(graph.graph[current_vertex][neighbour])

            if temp_route < distances[neighbour]:
                distances[neighbour] = temp_route
        unvisited.remove(current_vertex)
    result = {}
    
    for node in distances :
        result [node.value] = distances[node]
    print(result)



graph = CG.createGraph('city_data.txt')
src = graph.vertices[2]
dijkstra(graph,src)