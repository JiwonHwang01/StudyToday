import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, read().split())
visited = [False] * (n + 1)
board =[[0]*(n+1) for _ in range(n+1)]
cnt = 0


for _ in range(m):
    x, y = map(int, read().split())
    board[x][y] = 1
    board[y][x] = 1

def dfs(num):
    visited[num] = True

    for i in range(1,n+1):
        if board[num][i] == 1 and not visited[i]:
            dfs(i)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)