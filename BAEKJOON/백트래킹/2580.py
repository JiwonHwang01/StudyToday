import sys

read = sys.stdin.readline

board = [list(map(int,read().split())) for _ in range(9)]
zeroIndex = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeroIndex.append([i,j])

def checkColumn(y, num):
    for i in range(9):
        if board[i][y] == num:
            return False
    return True

def checkRow(x, num):
    for i in range(9):
        if board[x][i] == num:
            return False
    return True

def checkRect(x, y, num):
    dx = x // 3 * 3
    dy = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if board[i + dx][j + dy] == num:
                return False
    return True


def dfs(index):
    if index == len(zeroIndex):
        for i in range(9):
            print(" ".join(map(str,board[i])))
        exit(0)

    for num in range(1,10):
        x = zeroIndex[index][0]
        y = zeroIndex[index][1]

        if checkColumn(y, num) and checkRow(x, num) and checkRect(x, y, num):
            board[x][y] = num
            dfs(index+1)
            board[x][y] = 0
    
dfs(0)