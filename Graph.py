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

    def bfs(self, adjList, sourceVertex):

        (visited, parent, distance) = (dict(), dict(), dict())
        for u in adjList.keys:
            visited[u] = False
            parent[u] = -1
            distance[u] = -1
        
        explorationQueue = Queue()

        visited[sourceVertex] = True
        distance[sourceVertex] = 0
        explorationQueue.add(sourceVertex)

        while(not explorationQueue.isempty()):
            u = explorationQueue.delete()             
            for v in adjList[u]:
                if(not visited[v]):                   
                    visited[v] = True
                    parent[v] = u
                    distance[v] = distance[u] + 1
                    explorationQueue.add(v)
        
        return(parent, distance)
    
    def __dfs(self, adjList, color, parent, time_in, time_out, dfs_timer, u):

        time_in[u] = dfs_timer = dfs_timer + 1
        color[u] = 1

        for v in self.adjList[u]:
            if(color[v] == 0):
                parent[v] = u
                (color, parent, time_in, time_out, dfs_timer) = self.__dfs(adjList, color, parent, time_in, time_out, dfs_timer, v)
        
        color[u] = 2
        time_out[u] = dfs_timer = dfs_timer + 1

        return (color, parent, time_in, time_out, dfs_timer)


    def dfs(self, adjList, sourceVertex):

        dfs_timer = 0
        (color, parent, time_in, time_out) = (dict(), dict(), dict(), dict())
        for u in adjList.keys:
            (color[u], parent[u], time_in[u], time_out[u]) = (0, -1, 0, 0)
        
        return self.__dfs(adjList, color, parent, time_in, time_out, dfs_timer, sourceVertex)

               
