
import math
import create_Graph as CG


def heuristic(node ,destin):
    location =  {}   
    with open('heuristic.txt','r') as file: 
        for line in file:
            temp_list = line.split()
            location[temp_list[0]] = {"Latitude":eval(temp_list[1]),"Longitude":eval(temp_list[2])}
    lat_dif = location[destin.value]["Latitude"] - location[node.value]["Latitude"]
    long_dif = location[destin.value]["Longitude"] - location[node.value]["Longitude"]
    heurist = math.sqrt((lat_dif*lat_dif)+ (long_dif*long_dif))
    return heurist


def a_Star(graph ,src , destin):
    open_list = set([src])
    close_list =set([])

    dist_src = {src:0}
    parent = {src : src }
    while len(open_list) > 0:
        temp = None

        # find node with smallest f and modifiy temp
        for node in open_list:
            if temp == None or dist_src[node]+heuristic(node,destin) < dist_src[temp]+heuristic(node,destin):
                temp = node
        
        if temp == None:
            print("path does not exist")
            return None

        # if n is the final node reconstruct path and return 
        if temp == destin:
            reconst_path = []
            while parent[temp] != temp:
                reconst_path.append(temp.value)
                temp = parent[temp]
            reconst_path.append(src.value)
            reconst_path.reverse()
            # print("shortest path from {} to {} is : {}".format(src,destin,reconst_path))
            # print(reconst_path)
            return reconst_path

        # finding neibhors of current node
        for neibhor in graph[temp]:
            if neibhor not in open_list and neibhor not in close_list:
                open_list.add(neibhor)
                parent[neibhor] = temp
                dist_src[neibhor] = dist_src[temp]+int(graph[temp][neibhor])
            
            else:
                if dist_src[neibhor] > dist_src[temp]+int(graph[temp][neibhor]):
                    dist_src[neibhor] = dist_src[temp]+int(graph[temp][neibhor])
                    parent[neibhor] = temp

                    if neibhor in close_list:
                        close_list.remove(neibhor)
                        open_list.add(neibhor)
            

        open_list.remove(temp)   
        close_list.add(temp) 
    print("path does not exist")
    return None


graph = CG.createGraph('city_data.txt')

src = graph.vertices[7]
print(src)
destin = graph.vertices[15]
print(destin)
a_Star(graph.graph,src,destin)
