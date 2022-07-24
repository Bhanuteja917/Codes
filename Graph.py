from yaml import compose
from Queue import Queue

class Graph():

    def __init__(self, adjList):
        self.adjList = dict(adjList)
        self.keys = [x for x in adjList.keys()]
    
    def __getitem__(self, u):
        return self.adjList[u]

    def __str__(self):
        graph = []
        for u in self.keys:
            graph.append(str(u) + ":" + str(self.adjList[u]))
        return str(graph)

    def bfs(self, sourceVertex):

        (visited, parent, distance) = (dict(), dict(), dict())
        for u in self.keys:
            visited[u] = False
            parent[u] = -1
            distance[u] = -1
        
        explorationQueue = Queue()

        visited[sourceVertex] = True
        distance[sourceVertex] = 0
        explorationQueue.add(sourceVertex)

        while(not explorationQueue.isempty()):
            u = explorationQueue.delete()             
            for v in self.adjList[u]:
                if(not visited[v]):                   
                    visited[v] = True
                    parent[v] = u
                    distance[v] = distance[u] + 1
                    explorationQueue.add(v)
        
        return(parent, distance)
    
    def dfs(self, sourceVertex):

        dfs_timer = 0
        (color, parent, pre, post) = (dict(), dict(), dict(), dict())
        for u in self.keys:
            (color[u], parent[u], pre[u], post[u]) = (0, -1, 0, 0)
        
        return self.__dfs(color, parent, pre, post, dfs_timer, sourceVertex)

    def __dfs(self, color, parent, pre, post, dfs_timer, u):

        pre[u] = dfs_timer
        dfs_timer = dfs_timer + 1
        color[u] = 1

        for v in self.adjList[u]:
            print(self.adjList[u])
            if(color[v] == 0):
                parent[v] = u
                (color, parent, pre, post, dfs_timer) = self.__dfs(color, parent, pre, post, dfs_timer, v)
        
        color[u] = 2
        post[u] = dfs_timer
        dfs_timer = dfs_timer + 1

        return (color, parent, pre, post, dfs_timer)
    
    def components(self):
        
        component = {}
        for u in self.keys:
            component[u] = -1
        (compid, seen) = (0, 0)

        while seen <= max(self.keys):
            startVertex = min([i for i in self.keys if component[i] == -1])
            print(startVertex)
            visited = self.bfs(startVertex)[1]
            # print(visited)
            for i in visited.keys():
                if visited[i] >= 0:
                    seen += 1
                    component[i] = compid
            compid += 1
            
        return component
