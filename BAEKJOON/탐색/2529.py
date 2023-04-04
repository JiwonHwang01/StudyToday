#브루트포스
import sys
from itertools import permutations

read =sys.stdin.readline

k = int(read())
code = list(read().split())
permut = permutations(range(10),k+1)
res = []
for case in permut:
    flag = 0
    for i in range(k):
        if code[i] == '<':
            if case[i] > case[i+1]:
                break
        else:
            if case[i] < case[i+1]:
                break
        if i == k-1:
            flag = 1
    if flag:
        if len(res) < 3:
            res.append(case)
        else:
            res[1] = case
print(*res[1],sep='')
print(*res[0],sep='')
    
