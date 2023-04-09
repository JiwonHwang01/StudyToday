# DFS
import sys, copy

input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
res = 0

def left(board):
    for i in range(N):
        pos = 0
        for j in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pos] == 0:
                    board[i][pos] = tmp
                
                elif board[i][pos] == tmp:
                    board[i][pos] *= 2
                    pos += 1
                
                else:
                    pos += 1
                    board[i][pos] = tmp
    
    return board

def right(board):
    for i in range(N):
        pos = N-1
        for j in range(N-1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][pos] == 0:
                    board[i][pos] = tmp
                
                elif board[i][pos] == tmp:
                    board[i][pos] *= 2
                    pos -= 1
                
                else:
                    pos -= 1
                    board[i][pos] = tmp
    
    return board

def up(board):
    for j in range(N):
        pos = 0
        for i in range(1, N):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[pos][j] == 0:
                    board[pos][j] = tmp
                
                elif board[pos][j] == tmp:
                    board[pos][j] *= 2
                    pos += 1
                
                else:
                    pos += 1
                    board[pos][j] = tmp
    return board

def down(board):
    for j in range(N):
        pos = N-1
        for i in range(N-1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[pos][j] == 0:
                    board[pos][j] = tmp
                
                elif board[pos][j] == tmp:
                    board[pos][j] *= 2
                    pos -= 1
                
                else:
                    pos -= 1
                    board[pos][j] = tmp
    
    return board

def dfs(n, arr):
    global res

    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > res:
                    res = arr[i][j]
        return
    
    for i in range(4):
        copy_board = copy.deepcopy(arr)

        if i == 0:
            dfs(n + 1, left(copy_board))
        elif i == 1:
            dfs(n + 1, right(copy_board))
        elif i == 2:
            dfs(n + 1, up(copy_board))
        else:
            dfs(n + 1, down(copy_board))

dfs(0, board)
print(res)