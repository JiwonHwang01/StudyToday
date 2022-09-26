import sys

read = sys.stdin.readline

n = int(read())
dp = [0]*(n + 1)
s = [0]*(n + 1)

for i in range(1, n+1):
    s[i] = int(read())

dp[1] = s[1]

for i in range(2, n+1):

    if i == 2:
        dp[2] = s[1] + s[2]
        continue

    if i == 3:
        dp[3] = max(s[2] , s[1]) + s[3]
        continue

    dp[i] = max(dp[i-3] + s[i-1] , dp[i-2]) + s[i]
    
print(dp[n])
