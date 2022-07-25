# Consider a social network of friends/relatives, most of whom are closely connected.
# Visualize this as a graph where each vertex denotes a person, and if two people know 
# each other there is an edge between the vertices denoting them. If persons x and y 
# know each other directly, then there is an edge connecting x and y and level of 
# connectivity between them is 1. If person x is a friend of person y and person y is 
# friend of person z, but x is not a friend of z, then the level of connectivity between 
# x and z is 2, and so on. The connectivity between people is always two way, i.e. if x 
# directly knows y, then y also knows x directly.
# Complete the Python function findConnectionLevel (n, Gmat, Px, Py) that takes 4 arguments, 
# number of persons n (n persons numbered from 0 to n-1), Gmat an adjacency matrix representation 
# of n persons and their connections(if Gmat [x][y] = 1, then person x and y are directly connected), 
# two persons PX and Py both numbers, and returns the minimum level of connectivity between Px and Py. 
# Return 0 if Px and Py are not connected through anybody in the group.
# For example, for the graph below representing 7 persons from 0 to 6 and their connectivity.

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

n = int(input())
Amat = []
for i in range(n):
    row = [int(x) for x in input().split(" ")]
    Amat.append(row)

personX = int(input())
personY = int(input())

# print(Amat)
# print(personX, personY, n)

def neighbours(i ,Amat, n):
    return [j for j in range(n) if Amat[i][j] == 1]

def findConnectionLevel(n, Gmat, Px, Py):
    connection = [-1]*n
    explorationQueue = Queue()

    connection[Px] = 0
    explorationQueue.add(Px)

    while(not explorationQueue.isempty()):
        u = explorationQueue.delete()
        for v in neighbours(u, Amat, n):
            #print(neighbours(u, Amat, n))
            if connection[v] == -1:
                connection[v] = connection[u] + 1
                explorationQueue.add(v) 
    
    return connection[Py]
    
print(findConnectionLevel(n, Amat, personX, personY))