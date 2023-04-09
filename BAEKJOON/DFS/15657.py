import sys
read = sys.stdin.readline

n, m = map(int,read().split())
num = list(map(int,read().split()))
num.sort()
s = []

def dfs(depth, start):
    if depth == m:
        print(" ".join(map(str,s)))
        return
    last = 0
    for i in range(start, n):
        if last != num[i]:
            s.append(num[i])
            dfs(depth + 1, i)
            last = s.pop()

dfs(0, 0)