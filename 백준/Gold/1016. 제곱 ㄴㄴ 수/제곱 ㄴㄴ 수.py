# 1016
import sys
import time
read = sys.stdin.readline

mn, mx = map(int, read().split())
res = [i for i in range(mn, mx + 1)]

n = 2
count = 0

while n**2 < mx + 1:
    remain = mn %  n**2
    if remain:
        sp = n**2 - remain
    else:
        sp = 0
    
    for i in range(sp, mx -mn + 1, n**2):
        res[i] = False
    
    n += 1

for i in range(mx-mn+1):
    if res[i]:
        count += 1

print(count)