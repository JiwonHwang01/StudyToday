import sys
from collections import deque

read = sys.stdin.readline

m, n, h = map(int, read().split())
box = []

for i in range(h):
    box.append([list(map(int,read().split())) for _ in range(n)])

dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque()
tmp = 0
res = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                queue.append([j,i,k])
                tmp += 1

def bfs(box, queue, tmp, res):
    flag = True

    while queue:
        res += 1
        for _ in range(tmp):
            x, y, z = queue.popleft()

            for i in range(6):
                if x + dx[i] < 0 or x + dx[i] >= m or y + dy[i] < 0 or y + dy[i] >= n or z + dz[i] < 0 or z + dz[i] >= h:
                    continue
                if box[z + dz[i]][y + dy[i]][x + dx[i]] == -1 or box[z + dz[i]][y + dy[i]][x + dx[i]] == 1:
                    continue
                queue.append([x + dx[i],y + dy[i],z + dz[i]])
                box[z + dz[i]][y + dy[i]][x + dx[i]] = 1

        
        tmp = len(queue)
    res -= 1
    
    for k in range(h):
        if flag:
            for i in range(n):
                if flag:
                    for j in range(m):
                        if box[k][i][j] == 0:
                            res = -1
                            flag = False
                            break
                else:
                    break

    print(res)

bfs(box, queue, tmp, res)