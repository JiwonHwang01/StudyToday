# 2s
# N : 1 ~ 11
import sys

result = [int(1e9),int(-1e9)]
read = sys.stdin.readline
N = int(read())
a = list(map(int,read().split()))
o = list(map(int,read().split()))

def dfs(n, temp):
    if n == N-1:
        result[0] = min(result[0],temp)
        result[1] = max(result[1],temp)
        return
    
    if o[0] != 0:
        o[0] -= 1
        dfs(n+1, temp + a[n+1])
        o[0] += 1
    if o[1] != 0:
        o[1] -= 1
        dfs(n+1, temp - a[n+1])
        o[1] += 1
    if o[2] != 0:
        o[2] -= 1
        dfs(n+1, temp * a[n+1])
        o[2] += 1
    if o[3] != 0:
        o[3] -= 1
        dfs(n+1, int(temp / a[n+1]))
        o[3] += 1

dfs(0, a[0])
print(result[1])
print(result[0])