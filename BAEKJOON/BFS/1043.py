import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
know = list(map(int, read().split()))
num_know = know[0]

bfs = deque()
for num in know[1:]:
    bfs.append(num)

graph = []
visited = [False]* (1+n)
visited_party = [False] * m
res = 0

for i in range(m):
    party = list(map(int, read().split()))
    graph.append(party[1:])

while bfs:
    node = bfs.popleft()
    visited[node] = True

    for i in range(m):
        if node in graph[i]:
            for num in graph[i]:
                if not visited[num]:
                    bfs.append(num)
            visited_party[i] = True
                
for i in range(m):
    if not visited_party[i]:
        res += 1

print(res)