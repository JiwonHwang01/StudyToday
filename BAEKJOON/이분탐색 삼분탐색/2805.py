import sys

read = sys.stdin.readline
n, m = map(int,read().split())
trees = list(map(int, read().split()))
log = 0
res = 0

high, low = max(trees), 0
while high >= low:
    log = 0
    mid = ( high + low ) // 2
    
    for tree in trees:
        if tree > mid:
            log += tree - mid
        if log >= m:
            break

    if log >= m:
        res = mid
        low = mid + 1

    else: 
        high = mid - 1
        
print(res)