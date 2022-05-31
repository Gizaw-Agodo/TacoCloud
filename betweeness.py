
from turtle import Vec2D
import a_star as A
import create_Graph as CG
def betweeness (graph):
    vertices = graph.vertices
    for vertex in vertices:
       
        betweens = 0
        for vertex1 in vertices:
            visited = []
            if vertex1 == vertex :
                continue 
            visited.append(vertex1)
            for vertex2 in vertices:
                if vertex2 == vertex or vertex2 in visited or vertex2 == vertex1:
                    continue
                else:
                    short_path = A.a_Star(graph.graph,vertex1,vertex2)
                    if vertex.value in short_path[1:-1]:
                        calc_betweeness = 1
                        betweens += calc_betweeness
        print(vertex.value , betweens)

graph = CG.createGraph('city_data.txt')
print(graph.vertices[3])
betweeness(graph)
                    
