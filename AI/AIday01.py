#Hackerrank AI BOT Save the princess-2

def findPrincess(n, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                return (i,j)
    return (0,0)
def getDiff(t,x, mode = 'r'):
    if (mode == 'r'):
        return x-t[0]
    elif (mode == 'c'):
        return t[1]-x
    else:
        return 0
def nextMove(n,r,c,grid):
    pos = findPrincess(n, grid)
    row = getDiff(pos, r, mode='r')
    col = getDiff(pos, c, mode = 'c')
    #print(row, col)
    path = ""
    if row > 0:
        return "UP"
    elif row < 0:
        return "DOWN"
    if col>0:
        return "RIGHT"
    elif col < 0:
        return "LEFT"
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))