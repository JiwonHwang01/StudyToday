import sys

n, k = map(int, sys.stdin.readline().split())
count = 0

while True:
    if n == k:
        break
    
    if k % 2 == 1:
        k -= 1
    else:
        
        n += 1
    count += 1

print(n, k, count)