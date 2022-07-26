# Given an undirected graph G, write a Python function to compute the number of connected components. 
# A set of nodes form a connected component in an undirected graph if there exists a path between every pair of nodes in this set.
# Write a Python function find components_undirectedGraph (vertices, edges), that accepts a list of vertices and a list of tuples 
# that represent edges, and returns the number of connected components in the graph formed by vertices and edges. Each tuple (i,j) 
# in edges represents an edge between vertices i and j.For a completely connected graph there is only one connected component, 
# hence the function should return 1

vertices = [int(x) for x in input().split(" ")]
numOfEdges = int(input())
edges = []
for i in range(numOfEdges):
    edge = (int(x) for x in input().split(" "))
    edges.append(tuple(edge))
    
def adjList(vertices, edges):
    graph = {}

    for vertex in vertices:
        graph[vertex] = []

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    return graph

def dfs(graph, vertex):
    visited = {}
    for v in graph.keys():
        visited[v] = False
    return _dfs(graph, visited, vertex)

def _dfs(graph, visited ,v):
    visited[v] = True
    for u in graph[v]:
        if(not visited[u]):
            visited = _dfs(graph, visited, u)
    return visited 

def findComponents_undirectedGraph(vertices, edges):
    graph = adjList(vertices, edges)
    component = {}
    for v in graph.keys():
        component[v] = -1
    (compid, seen) = (0, 0)


    while seen <= (len(graph.keys()) - 1):
        startVertex = min([v for v in graph.keys() if component[v] == -1 ])
        visited = dfs(graph, startVertex)
        for v in visited.keys():
            if visited[v]:
                seen += 1
                component[v] = compid
        compid += 1
    
    return compid
    

print(findComponents_undirectedGraph(vertices, edges))

