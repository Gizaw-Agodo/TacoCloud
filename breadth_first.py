
# python implementation of breadth first search
import create_Graph as CG
import timeit

def breadthFirst( graph , node,destin):
    visited = []
    queue = [node]
    count = 0
    while queue:
        tempNode = queue.pop(0)
        for neighbhour in graph[tempNode]:
            if neighbhour not in visited:
                queue.append(neighbhour)
        if tempNode not in visited:
            visited.append(tempNode)
            count +=1 
            if tempNode == destin:
                return count


# graph = CG.createGraph('city_data.txt')
# node = graph.vertices[0]
# breadthFirst(graph.graph,node)


def iter(graph):
    mysum = 0
    for i in range(len(graph.vertices)):
        node = graph.vertices[i]
        for j in range(len(graph.vertices)):
            node2 = graph.vertices[j]
            mysum += breadthFirst(graph.graph,node,node2)

    print(mysum)
graph = CG.createGraph('city_data.txt')
iter(graph)



setup = """
import timeit
import create_Graph as CG
"""
code = """
graph = CG.createGraph('city_data.txt')
iter(graph.graph)

"""

print (timeit.timeit(setup = setup,
                    stmt = code,
                    number = 100000))