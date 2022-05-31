
from cmath import inf


def dijikstra(graph ,src ,destin):
    shortest_distance = {src:0}
    predecesor = {}
    unvisited = graph.vertices
    track_path = []

    for node in unvisited:
        shortest_distance[node] = inf
    
    while unvisited:
        min_distance = None
        for node in unvisited:
            if min_distance == None:
                min_distance = node
            elif shortest_distance[node] <shortest_distance[min_distance]:
                min_distance = node

