#!/usr/bin/python

# Head ends here
#path = ""

#Hackerrank AI BOT CLEAN partially observable

import random as r

def findDirtyCell(grid, currIndex):
    n = 5
    RANGE = 1
    posx = currIndex[0]
    posy = currIndex[1]
    dirty = []
    for i in range( max(0, posx - RANGE-1) , min(5, posx + RANGE+1)):
        for j in range( max(0, posy - RANGE-1) , min(5, posy + RANGE+1)):
            if grid[i][j] == 'd':
                dirty.append((i,j))
    return dirty
    
def getDiff(t,x, mode = 'r'):
    if (mode == 'r'):
        return x-t[0]
    elif (mode == 'c'):
        return t[1]-x
    else:
        return 0
def getBoundaryArray(currIndex):
    posx = currIndex[0]
    posy = currIndex[1]
    x = 0
    y = 0
    if posx == 0:
        x = -1
    elif posx == 4:
        x = 1
    if posy == 0:
        y = -1
    elif posy == 4:
        y = 1
    return (x,y)
    
def moveifNotReachable(currIndex):
    M = getBoundaryArray(currIndex)
    """
    vert = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    horz = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    """
    F = ['DOWN', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'LEFT', 'RIGHT', 'UP', 'LEFT']
    loc = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
    INDEX = loc.index(M)
    return F[INDEX]

def getDistance(currIndex, dirty):
    x= []
    y= []
    dist = []
    posr = currIndex[0]
    posc = currIndex[1]
    for dc in dirty:
        x.append(dc[0])
        y.append(dc[1])
        _dist = (dc[0] - posr)**2 + (dc[1] - posc)**2
        dist.append(_dist)
    return x, y, dist

def next_move(posx, posy, board):

    currIndex = (posx, posy)
    dirty = findDirtyCell(board, currIndex)
    
    (xList, yList, distList) = getDistance(currIndex, dirty)
    try:
        INDEX = distList.index(min(distList))
        TO = (xList[INDEX], yList[INDEX])
        row = getDiff(TO, currIndex[0], mode='r')
        col = getDiff(TO, currIndex[1], mode = 'c')
        
        #board[currIndex[0]][currIndex[1]] = "-"
        
        #print(row, col)
        path = ""
        if row > 0:
            print("UP")
            return 0
        elif row < 0:
            print("DOWN")
            return 0
        if col>0:
            print("RIGHT")
            return 0
        elif col < 0:
            print("LEFT")
            return 0
        elif col == 0 and row == 0:
            print("CLEAN")
            return 0

    except:
        print(moveifNotReachable(currIndex))
        """
        if posx>= 0 and posx<4:
            print("DOWN")
            return 0
        elif posx == 4:
            if posy>=0 and posy<4:
                print("RIGHT")
            elif posy == 4:
                print("UP")
                return 0
        if col==4:
            if posx>=0 and posx<4:
                print("UP")
            elif posx == 4:
                print("LEFT")
                return 0
        """
        """
        elif col < 0:
            print("LEFT")
            return 0
        elif col == 0 and row == 0:
            print("CLEAN")
            return 0
    """
# Tail starts here

if __name__ == "__main__":
    #fp1 = open("input.txt", "r")
    #input = fp1.read()
    #print (input)
    
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
    