# 1s
# N : 2 ~ 100, K : 2 ~ 100
import sys
from collections import deque

result = 0
read = sys.stdin.readline
N = int(read())
board = [[0]*N for _ in range(N)]
command = deque()
dx, dy = [1,0,-1,0], [0,1,0,-1]

K = int(read())
for i in range(K):
    y, x = map(int, read().split())
    board[y-1][x-1] = 1

L = int(read())
x, y = 0, 0
d = 0
q= deque()
q.append([x,y])
flag = False
count = 0

for i in range(L):
    t, c = read().split()
    t = int(t)
    command.append([t,c])

t, c_now= command.popleft()
while True:
    if count == t:
        if command:
            t, c= command.popleft()
        if c_now == 'D':
            d = (d+1)%4
        elif c_now == 'L':
            d = (d-1)%4
        c_now = c
    result += 1
    nx, ny = x+dx[d], y+dy[d]
    if 0<=nx<N and 0<=ny<N:
        if board[ny][nx] < 0:
            flag = True
            break
        
        q.append([nx,ny])
        if board[ny][nx] == 0:
            tail = q.popleft()
            board[tail[1]][tail[0]] = 0
        board[ny][nx] = -1
        x, y = nx, ny
        count+=1
    else:
        flag = True
        break

print(result)