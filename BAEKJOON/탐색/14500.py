# 14500 Tetromino dfs
import sys
read = sys.stdin.readline

n, m = map(int, read().split())

board = [list(map(int,read().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
res = 0

def dfs(x, y, pos, sum):
    global res
    visited[x][y] = True
    
    if pos == 3:
        res = max(res, sum)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if pos == 1:
                visited[nx][ny] = True
                dfs(x, y, pos+1, sum + board[nx][ny])

            visited[nx][ny] = True
            dfs(nx, ny, pos+1, sum + board[nx][ny])
            visited[nx][ny] = False

for i in range(n): # 세로
    for j in range(m): # 가로
        visited[i][j] = True
        dfs(i, j, 0, board[i][j])
        visited[i][j] = False

print(res)