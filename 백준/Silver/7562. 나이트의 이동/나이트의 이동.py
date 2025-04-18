# 7562

import sys
from collections import deque

read = sys.stdin.readline
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)]
T = int(read())

for _ in range(T):
    I = int(read())
    visited = [[False]*I for _ in range(I)]
    board = [[int(1e9)]*I for _ in range(I)]
    px, py = map(int,read().split())
    dx, dy = map(int,read().split())

    q = deque()
    q.append([px,py])
    visited[px][py] = True
    board[px][py] = 0

    while q:
        nx, ny = q.popleft()
        if nx == dx and ny == dy:
             break
        for i in range(8):
                kx, ky =  nx + moves[i][0], ny + moves[i][1]
                if 0<=kx<I and 0<=ky<I and not visited[kx][ky]:
                    q.append([kx, ky])
                    visited[kx][ky] = True
                    board[kx][ky] = board[nx][ny]+1

    print(board[dx][dy])