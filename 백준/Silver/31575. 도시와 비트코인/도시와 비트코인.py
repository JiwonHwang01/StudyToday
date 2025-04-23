from collections import deque
import sys

read = sys.stdin.readline

N, M = map(int,read().split())
board = [[] for _ in range(M)]

for i in range(M):
    board[i] = list(map(int,read().split()))

visited = [[False]*N for _ in range(M)]
q= deque()
q.append([0,0])
res = 'No'
dx, dy = [0,1], [1,0]
visited[0][0] = True

while q:
    pos_x, pos_y = q.popleft()

    if pos_x == N-1 and pos_y == M-1:
        res = 'Yes'
        break
    for i in range(2):
        nx, ny = pos_x + dx[i], pos_y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[ny][nx] and board[ny][nx] == 1:
                visited[ny][nx] = True
                q.append([nx,ny])
print(res)