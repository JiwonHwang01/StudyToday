# 16236 아기상어
import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
board = [list(map(int, read().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
res = 0
x, y, size = -1, -1, 2

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j
            break
    if x >= 0:
        break

def sharkToFish(x, y, size):
    time = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    fish = []

    while queue:
        pos_x, pos_y = queue.popleft()
        
        for i in range(4):
            nx = pos_x + dx[i]
            ny = pos_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= size:
                    queue.append([nx,ny])
                    time[nx][ny] = time[pos_x][pos_y] + 1
                    visited[nx][ny] = True
                
                    if 0 < board[nx][ny] < size:
                        fish.append([nx, ny, time[nx][ny]])

    fish.sort(key = lambda x: (-x[2], -x[0], -x[1]))
    return fish

flag = 0

while True:
    fish = sharkToFish(x, y, size)

    if not fish:
        break
    
    nx, ny, time = fish.pop()

    res += time
    board[x][y] = 0
    board[nx][ny] = 0
    
    x, y = nx, ny

    flag += 1
    if flag == size:
        flag = 0
        size += 1

print(res)