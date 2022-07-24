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

graph = Graph(adjList)

result = graph.bfs(graph, 7)

print(result[0], result[1])
# print(graph)
# print(graph.keys)
# print(type(graph.keys))