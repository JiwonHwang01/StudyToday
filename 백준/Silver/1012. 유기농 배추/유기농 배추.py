#1012
import sys
from collections import deque
sys.setrecursionlimit(10000)


read = sys.stdin.readline
T = int(read())

dx, dy= [0, 0, 1, -1], [1, -1, 0, 0]

def dfs(x, y, M, N):
    for i in range(4):
        nx ,ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[ny][nx] and board[ny][nx] == 1:
                visited[ny][nx] = True
                dfs(nx, ny, M, N)

for _ in range(T):
    M, N, K = map(int,read().split())

    board = [[0]*M for _ in range(N)]
    q= deque()
    visited = [[False]*M for _ in range(N)]
    res = 0
    for i in range(K):
        x, y = map(int,read().split())
        board[y][x] = 1
        q.append([x,y])
    while q:
        x, y = q.pop()
        if not visited[y][x]:
            res += 1
            
            dfs(x, y, M, N)
    print(res)