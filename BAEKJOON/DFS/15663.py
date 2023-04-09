import sys
read = sys.stdin.readline

n, m = map(int,read().split())
num = list(map(int,read().split()))
num.sort()
s = []
visited = [False] * n

def dfs(depth):
    if depth == m:
        print(" ".join(map(str,s)))
        return
    last = 0
    for i in range(n):
        if not visited[i] and last != num[i]:
            s.append(num[i])
            visited[i] = True
            dfs(depth + 1)
            last = s.pop()
            visited[i] = False

dfs(0)