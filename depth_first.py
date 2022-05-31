
import timeit
import create_Graph as CG

# binary search function
def depthFirst(graph,node,destin):
    stack = [node]
    visited = []
    while len(stack) != 0:
        node1 = stack.pop()
        if node1 not in  visited : 
            visited.append(node1)
            if node1 == destin:
                [visited.value for visited in visited]
        for node in graph[node1]:
            if node not in visited:
                stack.append(node)
    return 




setup = """
import timeit
import create_Graph as CG
"""
code = """
graph = CG.createGraph('city_data.txt')
def depthFirst(graph,node,destin):
    stack = [node]
    visited = []
    while len(stack) != 0:
        node1 = stack.pop()
        if node1 not in  visited : 
            visited.append(node1)
            if node1 == destin:
                [visited.value for visited in visited]
        for node in graph[node1]:
            if node not in visited:
                stack.append(node)
    return 
"""

print (timeit.timeit(setup = setup,
                    stmt = code,
                    number = 100000))
    




































# # python implementation of depth first search
# import timeit
# import create_Graph as CG




    
# # visited  = depthFirst(graph.graph,node,)




# #








