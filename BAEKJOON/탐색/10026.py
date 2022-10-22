# 10026 적록색약 BFS
import sys
from collections import deque

def bfs(x, y):
    queue = deque([[x,y]])
    visited[x][y] = True

    while queue:
        x, y = list(queue.popleft())

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]: 
                if board[nx][ny] == board[x][y]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    
read = sys.stdin.readline
n = int(read())

board = [list(read()) for _ in range(n)]
visited = [[False]*n for _ in range(n)] 
res = [0, 0]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            res[0] += 1

visited = [[False]*n for _ in range(n)] 

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):        
        if not visited[i][j]:
            bfs(i, j)
            res[1] += 1

print(res[0], res[1])