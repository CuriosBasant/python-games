# Please input two integers (m, n) to
# create a m*n maze, for n less than 20,
# because it will broken in SoloLearn
# output area.
#
# I also add the solution for the maze.
# It shows not only path but directions.
# However, due to limited showable chars
# I can't show the path when there's a wall
# under it.
#
# Enjoy playing it. (((*´꒳`*)))
#
#                              '18/05/07
#                  Flandre Scarlet(雨宮 桜)
#

solOn = True # Set True with solution

import random

def CreateMap(m, n):
    gamemap = []
    for p in range(m):
        line = []
        for q in range(n):
            line.append([1,1])
        gamemap.append(line)
    return gamemap

def CreatePuzzle(gamemap, m, n):
    path = sol = [[0,0]]
    number = 1 # associated places
    area = m*n # total grids
    i = 0 # index for path
    #j = 0 # ways back
    
    while number < area:
        x, y = path[i][0], path[i][1] # current grid
        # go back if there's no more way
        while(( x==m-1 or [x+1,y] in path) and ( y==n-1 or [x,y+1] in path) 
            and ( x==0 or [x-1,y] in path) and ( y==0 or [x,y-1] in path)):
            if sol[-1]==path[i] and sol[-1]!=[m-1,n-1]:
                del sol[-1]
            i -= 1
            x, y = path[i][0], path[i][1]
        
        dir = random.randint(0,3) # direction
        
        if dir == 0: # down
            if x+1==m: # out of the map
                continue
            if [x+1,y] in path:
                continue # choose dir again
            else:
                gamemap[x][y][0]=0
                sol.append([x+1,y])
                path.append([x+1,y])
                i = number
                number += 1
                
        elif dir == 1: # right
            if y+1==n: # out of the map
                continue
            if [x,y+1] in path:
                continue # choose dir again
            else:
                gamemap[x][y][1]=0
                sol.append([x,y+1])
                path.append([x,y+1])
                i = number
                number += 1
                
        elif dir == 2: # up
            if x==0: # out of the map
                continue
            if [x-1,y] in path:
                continue # choose dir again
            else:
                gamemap[x-1][y][0]=0
                sol.append([x-1,y])
                path.append([x-1,y])
                i = number
                number += 1

        elif dir == 3: # left
            if y==0: # out of the map
                continue
            if [x,y-1] in path:
                continue # choose dir again
            else:
                gamemap[x][y-1][1]=0
                sol.append([x,y-1])
                path.append([x,y-1])
                i = number
                number += 1

    map[m-1][n-1][1]=0 # open the exit
    print(*gamemap,'',sol, sep='\n')
    return sol

def DrawMap(gamemap, m, n, sol = []):
    print(" V "+"_ "*(n-1))
    for p in range(m-1):
        line = "|"
        for q in range(n):
            line += ("_" if gamemap[p][q][0]==1 else " " if [p,q] not in sol else "^" if sol[sol.index([p,q])+1]==[p-1,q] else "v" if sol[sol.index([p,q])+1]==[p+1,q] else ">" if sol[sol.index([p,q])+1]==[p,q+1] else "<") + (" " if gamemap[p][q][1]==0 else "|")
        print(line)
"""
    line = "|" # last line
    for q in range(n):
        line += "_" + (" " if gamemap[m-1][q][1]==0 else "|")
    print(line + ">") # exit
"""
while True:
    m = int(input('Height: '))
    try:
        n = int(input('Width: '))
    except:
        n = m
    if m<1 or n<1:
        print("The maze size can't be that strange >~<")
    else:
        map = CreateMap(m,n)
        sol = CreatePuzzle(map, m, n)
        while sol[-1]!=[m-1,n-1]:
            del sol[-1]
        DrawMap(map, m, n, sol if solOn else [])
    yn=input('Do you want to continue :')
    if yn=='n':
        break