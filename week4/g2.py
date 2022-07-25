# Consider a system of n water tanks on a hill, connected via m pipes. Water can flow through these pipes only in one direction. 
# We have a source of water that can be connected to only one of these water tanks. We need to find if there exists a master tank
#  such that all the tanks in this group can be filled by connecting the water source to this master tank. The tanks are numbered 
# from 1 to n.
# Write a Python function findMasterTank (tanks, pipes) that accepts arguments tanks which is a list of tanks, and pipes which is a 
# list of tuples that represents connectivity through pipes, between tanks. Each tuple (i,j) in pipes represents a pipe such that,
# water can flow from tank i to tank j but not vice versa. Your function should find a master tank and return the number representing it, 
# else should return 0 if no master tank exists in the system. If there are more than one master tanks return any one of them. 
# Try to implement an algorithm that executes in linear time (O(n + m)).

tanks = [int(x) for x in input().split(" ")]
noOfPipes = int(input())
pipes = []
for i in range(noOfPipes):
    pipe = (int(x) for x in input().split(" "))
    pipes.append(tuple(pipe))

def adjList(vertices, edges):
    graph = {}

    for vertex in vertices:
        graph[vertex] = []

    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    return graph


def findMasterTank(tanks, pipes):
    gList = adjList(tanks, pipes)
    indegree = {}
    for u in gList.keys():
        indegree[u] = 0
    
    for u in gList.keys():
        for v in gList[u]:
            indegree[v] += 1
    
    print(indegree)

    masterTank = 0
    count = 0
    for u in gList.keys():
        if indegree[u] == 0:
            count += 1
            masterTank = u

    
    if count != 1:
        return 0
    else:
        return masterTank


print(findMasterTank(tanks, pipes))