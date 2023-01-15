import sys
from collections import deque

read = sys.stdin.readline

v = int(read())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for i in range(1,v):
    edge = list(map(int,read().split()))
    node_num = edge[0]

    graph[node_num].append((edge[1],edge[2]))
    graph[edge[1]].append((node_num, edge[2]))

distance = [0] * (v+1)

def bfs(start):
    queue = deque()
    queue.append(start)

    visited[start] = True
    while queue:
        node = queue.popleft()
        for edge in graph[node]:
            if not visited[edge[0]]:
                queue.append(edge[0])
                visited[edge[0]] = True
                distance[edge[0]] = distance[node] + edge[1]

bfs(1)
res_index = distance.index(max(distance))
visited = [False] * (v+1)
distance = [0] * (v+1)
bfs(res_index)
print(max(distance))