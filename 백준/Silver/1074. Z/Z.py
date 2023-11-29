# 1074 Z
import sys

read = sys.stdin.readline

n, r, c = map(int, read().split())
res = 0

r, c = r + 1, c + 1

while True:
    if n == 0:
        break
    
    if r > 2**(n-1):
        res += 2**(n-1) * 2**(n-1) * 2
        r -= 2**(n-1)
    
    if c > 2**(n-1):
        res += 2**(n-1) * 2**(n-1)
        c -= 2**(n-1)
    
    n = n-1

print(res)