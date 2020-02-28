#!/usr/bin/python

#Hackerrank AI BOT Save the princess
def displayPathtoPrincess(n,grid):
    topLeft = grid[0][0]
    topRight = grid[0][n-1]
    bottomLeft = grid[0][n-1]
    bottomRight = grid[n-1][n-1]
    if(topLeft == 'p'):
        for i in range(int(n/2)):
            print('UP')
        for i in range(int(n/2)):
            print('LEFT')
    elif(topRight == 'p'):
        for i in range(int(n/2)):
            print('UP')
        for i in range(int(n/2)):
            print('RIGHT')
    elif(bottomLeft == 'p'):
        for i in range(int(n/2)):
            print('DOWN')
        for i in range(int(n/2)):
            print('LEFT')
    elif(bottomRight == 'p'):
        for i in range(int(n/2)):
            print('DOWN')
        for i in range(int(n/2)):
            print('RIGHT')
        
#print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)