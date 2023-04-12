import sys

read = sys.stdin.readline

n, m = map(int, read().split())
num = list(map(int, read().split()))
num.append(0)
cnt = [0] * m
res = 0

for i in range(n):
    num[i] += num[i-1]
    cnt[num[i]%m] += 1

res = cnt[0]

for k in cnt:
    res += k * (k-1) // 2

print(res)