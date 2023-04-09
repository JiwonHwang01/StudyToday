from itertools import permutations
import sys

read = sys.stdin.readline

count= int(read())
w = [list(map(int,read().split())) for _ in range(count)]

res = 10000000
flag = True

for p in permutations(range(count),count):
    if p[0] != 0:
        continue

    sum = 0
    flag = True
    for i in range(count):
        if sum > res:
            break

        if w[p[i]][p[(i+1)%(count)]] == 0:
            flag = False
            break
        
        sum += w[p[i]][p[(i+1)%(count)]]
    if flag:            
        res = min(res, sum)

print(res)