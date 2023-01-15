# 1208
import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int,input().split())
num = list(map(int,input().split()))
num1 = num[:N//2]
num2 = num[N//2:]
sum1 = []
sum2 = []
for i in range(len(num1)+1):
    combination = combinations(num1, i)
    for comb in combination:
        sum1.append(sum(comb))

for i in range(len(num2)+1):
    combination = combinations(num2,i)
    for comb in combination:
        sum2.append(sum(comb))

sum1.sort()
sum2.sort(reverse=True)

res = 0
p1, p2 = 0, 0

def countNum(arr, idx):
    target = arr[idx]
    count = 0
    while idx < len(arr) and arr[idx] == target:
        count += 1
        idx += 1
    
    return count 

while p1 < len(sum1) and p2 < len(sum2):
    #print("p1:", p1, "p2:", p2, "sum:", sum1[p1] + sum2[p2])
    if sum1[p1] + sum2[p2] == S:
        count1 = countNum(sum1, p1)
        count2 = countNum(sum2, p2)
        
        p1 += count1
        p2 += count2
        
        res += count1 * count2

    elif sum1[p1] + sum2[p2] < S:
        p1 += 1
    else:
        p2 += 1

if S == 0:
    res -= 1

print(res)