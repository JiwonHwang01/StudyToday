# 2s
# N : 1 ~ 100
import sys
from collections import deque
result = 0
read = sys.stdin.readline
wheel = ['']
for _ in range(4):
    wheel.append(read().rstrip())
K = int(read())
command = []
for _ in range(K):
    command.append(list(map(int,read().split())))

pos = [0,0,0,0,0]
q = deque()

for c in command:
    visited = [False]*5
    visited[c[0]] = True
    q.append(c)
    pos[c[0]] = (pos[c[0]] - c[1]) % 8
    while q:
        w, d = q.popleft()
        if w - 1 > 0:
            if not visited[w-1] and wheel[w][(pos[w]+d-2)%8] != wheel[w-1][(pos[w-1]+2)%8]:
                pos[w-1] = (pos[w-1] + d) % 8
                visited[w-1]= True
                q.append([w-1,-d])
        if w + 1 <= 4:
            if not visited[w+1] and wheel[w][(pos[w]+d+2)%8] != wheel[w+1][(pos[w+1]-2)%8]:
                pos[w+1] = (pos[w+1] + d) % 8
                visited[w+1] = True
                q.append([w+1,-d])
    
for i in range(1,5):
    if wheel[i][pos[i]] == '1':
        result += 2**(i-1)
    
print(result)