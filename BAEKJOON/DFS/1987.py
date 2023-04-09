#DFS - pypy로만 통과 가능
import sys

read = sys.stdin.readline
r, c = map(int,read().split())
board = ["" for _ in range(r)]
visited = [False] * 26
res = 0
for i in range(r):
    board[i] = read()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, count):
    global res  
    res = max(res, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not visited[ord(board[nx][ny]) -65]:
            visited[ord(board[nx][ny]) - 65] = True
            dfs(nx, ny, count+1)
            visited[ord(board[nx][ny]) - 65] = False

visited[ord(board[0][0])-65] = True
dfs(0,0,1)
print(res)