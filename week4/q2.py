# Complete the Python function findAllPaths to find all possible paths from the source vertex to destination vertex in a directed graph.
# Function findAllPaths(vertices, gList, source, destination) takes vertices as a list of vertices, gList a dictionary that is an adjacency 
# List representation of graph edges, source vertex, destination vertex, and returns a list of all paths from source to destination. The return 
# value will be a List of Lists, where every path is a sequence of vertices as a List. Return an empty list if no path exists from 'source' to 'destination'.

vertices = input().split(" ")
graph = {}
for v in vertices:
    graph[v] = input().split(" ")

(source, destination) = (input(), input())

def findAllPaths(vertices, gList, source, destination):
    visited = {}
    for v in vertices:
        visited[v] = False
    (path, result) = ([], [])
    return _findAllPaths(gList, source, destination, visited, path, result)[-1]

def _findAllPaths(gList, u, d, visited, path, result):
    visited[u] = True
    path.append(u)

    if u == d:
        result.append(path[:])
    else:
        for v in gList[u]:
            if not visited[v]:
                (gList, visited, path, result) = _findAllPaths(gList, v, d, visited, path, result)
    path.pop()
    visited[u] = False
    return (gList, visited, path, result)

print(findAllPaths(vertices, graph, '1', '2'))