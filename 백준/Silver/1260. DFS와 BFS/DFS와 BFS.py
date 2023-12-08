import sys
from collections import deque

read = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m, v = map(int, read().split())
visited = [False] * (n + 1)
board =[[0]*(n+1) for _ in range(n+1)]
cnt = 0


for _ in range(m):
    x, y = map(int, read().split())
    board[x][y] = 1
    board[y][x] = 1

def dfs(num):
    visited[num] = True
    print(num, end = " ")

    for i in range(1,n+1):
        if board[num][i] == 1 and not visited[i]:
            dfs(i)

def bfs(num):
    queue = deque([num])
    visited[num] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for i in range(1,n+1):
            if board[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)