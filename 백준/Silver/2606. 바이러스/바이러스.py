import sys
from collections import deque

read = sys.stdin.readline

N = int(read())
M = int(read())
graph = [[] for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (N+1)
q= deque()
q.append(1)
count = -1

while q:
    vortex = q.popleft()

    if not visited[vortex]:
        visited[vortex] = True
        q+=graph[vortex]
        count += 1
        
print(count)