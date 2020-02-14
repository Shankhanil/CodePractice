#!/usr/bin/python

# Head ends here
#path = ""

#Hackerrank AI BOT CLEAN
def findDirtyCell(grid):
    n = 5
    dirty = []
    for i in range(5):
        for j in range(5):
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
"""
def travel(FROM, TO):
    row = getDiff(TO, FROM[0], mode='r')
    col = getDiff(TO, FROM[1], mode = 'c')
    #print(row, col)
    path = ""
    if row > 0:
        print("UP")
    elif row < 0:
        print("DOWN")
    if col>0:
        print("RIGHT")
    elif col < 0:
        print( "LEFT")
    
    return TO
 """
def next_move(posr, posc, board):
    dirty = findDirtyCell(board)
    
    currIndex = (posr, posc)
    
    (xList, yList, distList) = getDistance(currIndex, dirty)
    INDEX = distList.index(min(distList))

    #INDEX = distList.index(min(distList))
    #currIndex = travel(FROM = currIndex, TO = (xList[INDEX], yList[INDEX]))
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

# Tail starts here

if __name__ == "__main__":
    #fp1 = open("input.txt", "r")
    #input = fp1.read()
    #print (input)
    
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
    