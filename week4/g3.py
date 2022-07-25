import ast

class Queue:
    def __init__(self):
        self.queue = []
    
    def add(self, v):
        self.queue.append(v)
    
    def delete(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def isempty(self):
        return self.queue == []
    
    def __str__(self):
        return(str(self.queue))

map = ""
for line in iter(input, map):
    map += line
map = ast.literal_eval(map)
#print(type(map))

def longJourney(map):
    (indegree, longestPath, parent) = ({}, {}, {})

    for city in map.keys():
        (indegree[city], longestPath[city], parent[city]) = (0, 0, "")

    for city in map.keys():
        for neighbourCity in map[city]:
            indegree[neighbourCity] += 1

    zeroDegreeQueue = Queue()
    for city in indegree.keys():
        if indegree[city] == 0:
            zeroDegreeQueue.add(city)

    while(not zeroDegreeQueue.isempty()):
        city = zeroDegreeQueue.delete()
        indegree[city] -= 1
        for neighbourCity in map[city]:
            indegree[neighbourCity] -= 1
            if(longestPath[neighbourCity] < (longestPath[city] + 1)):
                longestPath[neighbourCity] = longestPath[city] + 1
                parent[neighbourCity] = city
            if indegree[neighbourCity] == 0:
                zeroDegreeQueue.add(neighbourCity)
    return _longJourney(longestPath, parent)
    
def _longJourney(longestPath, parent):
    source = list(longestPath.keys())[0]
    destination = list(longestPath.keys())[1]
    for city in longestPath.keys():
        if longestPath[city] > longestPath[destination]:
            destination = city
        if longestPath[city] < longestPath[source]:
            source = city
    #print(source, destination)

    lpath = []
    lpath.append(destination)

    while(not parent[destination] == ""):
        lpath.append(parent[destination])
        destination = parent[destination]

    return list(reversed(lpath))


print(longJourney(map))




