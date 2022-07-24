import Queue

class Graph():
    def __init__(self, adjList):
        self.adjList = adjList
    
    explorationQueue = Queue()

    def bfs(self, adjList, sourceVertex):
        (visited, parent, distance) = (dict(), dict(), dict())
        for u in adjList.keys():
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
        
        return(parent, distance)
               
