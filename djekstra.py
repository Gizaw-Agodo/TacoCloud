from cmath import inf
import create_Graph as CG
import timeit

# graph = CG.createGraph('city_data.txt')

# def dijekistra_algorithm(Graph,src ,dest):
#     graph  = Graph.graph
#     min_distance = {src : 0}
#     for vertex in Graph.vertices :
#         min_distance[vertex] = inf 
    
#     visited = []
#     temp = src 
#     unvisited = Graph.vertices
    
#     while(len(unvisited)!=0):
#         if temp not in visited:
#             unvisited.remove(temp)
#             visited.append(temp)
            
#             min_heap = []
#             for v in unvisited:
#                 min_heap.append([v,min_distance[v]])

#             for j in graph[temp]:
#                 if j not in visited:
#                     min_heap.remove([j,min_distance[j]])
#                     distance = min_distance[temp]+ int(graph[temp][j])
#                     if distance < min_distance[j]:
#                         min_distance[j] =distance                    
#                     min_heap.append([j,min_distance[j]])
            
#             if len(min_heap)!=0:
#                 min = min_heap[0]
#                 for value in min_heap:
#                     if value[-1] < min[-1]:
#                         min = value
#                 temp = min[0]

#     print("minimum distance :"+ str(min_distance[dest]))
#     # print( vertex_data[dest]["prev"]+[dest])
#     print(min_distance)
#     print(unvisited)


def dijkstra(graph, src):
    distances = { }
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

    return(distances)


# graph = CG.createGraph('city_data.txt')
# src = graph.vertices[2]
# dijkstra(graph,src)



# def iter(graph):
#     mysum = 0
#     for i in range(len(graph.d)):
#         node = graph.vertices[i]
#         for j in range(len(graph.vertices)):
#             node2 = graph.vertices[j]
#             mysum += dijkstra(graph,node)

#     print(mysum)


# iter(graph)


setup = """
import timeit
import create_Graph as CG
"""
code = """
graph = CG.createGraph('city_data.txt')
for i in range(len(graph.vertices)):
    src = graph.vertices[i]
        
    def dijkstra(graph, src):
        distances = { }
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

        print(distances)
        
"""

print (timeit.timeit(setup = setup,
                    stmt = code,
                    number = 100000))