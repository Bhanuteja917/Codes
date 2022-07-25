# Maze solver
# Alice wants to find the key in a maze and get out of it. The maze representation is given below, where x represents walls, space represents the allowed 
# tiles Alice can walk on and represents the tile that has the key.
# • There is only one tile opening in the left-most vertical wall, where Alice is initially standing.
# Similarly there is only one tile opening in the right-most vertical wall, from which Alice has to exit.
# • Alice can travel horizontally or vertically, but cannot travel diagonally. Moving to adjacent tile vertically or horizontally is counted as a step.
# There are three possible outcomes, either you can exit the maze after getting the key, or the key is not reachable or the finish tile is not reachable.
# • Print the minimum number of steps Alice requires to reach the finish tile traveling through tile having the key.
# • If the key tile is not reachable then print -1.
# • If the key tile is reachable but finish tile is not reachable then print -2.
# Note: Input and printing are required
flag = True
maze = []
while(flag):
    line = input()
    if line:
        row = []
        for c in len(line):
            if c == 'X':
                row[c] = 0
            elif c == " ":
                row[c] = 1
            elif c == "*":
                row[c] = 2
        maze.append(row)
    else:
        flag = False
