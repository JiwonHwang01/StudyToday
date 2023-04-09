import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
board = [list(map(int,list(read().rstrip()))) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
res = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny]:
                queue.append([nx,ny])
                count += 1
                visited[nx][ny] = True

    res.append(count)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            bfs(i,j)

print(len(res))
res.sort()
print(*res,sep="\n")