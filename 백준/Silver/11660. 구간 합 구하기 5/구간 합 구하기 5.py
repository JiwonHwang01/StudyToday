# 11660
import sys
read = sys.stdin.readline
N, M = map(int, read().split())

board = [[] for _ in range(N)]
sum_board  = [[0]*(N+1) for _ in range(N+1)]

def minusOne(num):
    return num-1

for i in range(N):
    board[i] = list(map(int,read().split()))

for i in range(N):
    for j in range(N):
        sum_board[i+1][j+1] = board[i][j]
        if i > 0:
            sum_board[i+1][j+1] += sum_board[i][j+1]
        if j > 0:
            sum_board[i+1][j+1] += sum_board[i+1][j]
        if i > 0 and j > 0:
            sum_board[i+1][j+1] -= sum_board[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(minusOne,map(int, read().split()))
    print(sum_board[x2+1][y2+1] - sum_board[x1][y2+1] - sum_board[x2+1][y1] + sum_board[x1][y1])

'''
[1 3 6 10]
[3 8 15 24]
[6 15 27 42]
[10 24 42 64]
'''

'''
부분합 board 구하고
(x2, y2) - (x1,y2) - (x2, y1) + (x1, y1)
'''