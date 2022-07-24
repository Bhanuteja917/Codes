from Queue import Queue

class Graph():

    def __init__(self, adjList):
        self.adjList = dict(adjList)
        self.keys = [x for x in adjList.keys()]
    
    def __getitem__(self, u):
        return self.adjList[u]

    explorationQueue = Queue()

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

    def __str__(self):
        graph = []
        for u in self.keys:
            graph.append(str(u) + ":" + str(self.adjList[u]))
        return str(graph)
               
