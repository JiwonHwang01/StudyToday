from itertools import permutations
import sys

read = sys.stdin.readline

count= int(read())
num_list = list(map(int,read().split()))

res = 0
for p in permutations(num_list,count):
    res_tmp = 0
    for i in range(count-1):
        res_tmp += abs(p[i]-p[i+1])
    
    res = max(res,res_tmp)

print(res)