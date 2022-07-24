import re
from Graph import Graph

adjList = {
    0 : [1, 2, 4],
    1 : [0, 2],
    2 : [0, 1],
    3 : [4, 5, 6],
    4 : [0, 3, 7],
    5 : [3, 6, 7, 8],
    6 : [3, 5],
    7 : [4, 5, 8],
    8 : [5, 7, 9],
    9 : [8]
}

adjList2 = {
    0 : [1, 4],
    1 : [0],
    2 : [3, 6, 7],
    3 : [2, 7],
    4 : [0, 8, 9],
    5 : [],
    6 : [2, 7, 10],
    7 : [2, 3, 6, 10, 11],
    8 : [4, 9],
    9 : [8, 4],
    10 : [6, 7],
    11 : [7]
}

graph = Graph(adjList)
graph2 = Graph(adjList2)

result = graph2.dfs(0)

print(graph2.keys)
print(graph2)
print("color : " + str(result[0]))
print("parent : " + str(result[1]))
print("pre : " + str(result[2]))
print("post : " + str(result[3]))
print("dfs_timer : " + str(result[4]))
# print(graph)
# print(graph.keys)
# print(type(graph.keys))