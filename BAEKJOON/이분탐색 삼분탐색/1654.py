import sys

read = sys.stdin.readline
k, n = map(int,read().split())
line = [0]*k
count = 0
res = 0
for i in range(k):
    line[i] = int(read())

max, min = max(line), 1
while max >= min:
    count = 0
    mid = ( max + min ) // 2
    
    for l in line:
        count += l // mid

    if count >= n:
        res = mid
        min = mid + 1

    else: 
        max = mid - 1
        
print(res)