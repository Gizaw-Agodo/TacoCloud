import Graph as ajl
from breadth_first import bfs
def bfs_shortP(graph , start , goal):
    explored = []
    queue = [[start]]

    if start == goal :
        print ("the same node")
        return
    
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neibghbhors = graph(node)
            for neibhor in neibghbhors :
                new_path = path.append(neibhor)
                queue.append(new_path)

                if neibhor == goal:
                    return new_path
            explored.append(node)

path = bfs_shortP(ajl.graph.adj_list,ajl.node1,ajl.node3)
print(path)
ajl.Graph