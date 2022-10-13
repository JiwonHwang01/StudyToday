import sys

read = sys.stdin.readline

n = int(read())
t = [0] * (n+2)
p = [0] * (n+2)
dp = [0] * (n+2)
tmp = 0

for i in range(1,n+1):
    t[i],p[i] = map(int,read().split())
    t[i] += i

#print(t)
for i in range(1,n+1):
    tmp = max(dp[i],tmp)

    if t[i] > n+1:
        continue

    dp[t[i]] = max(dp[t[i]], tmp + p[i])

print(max(dp))