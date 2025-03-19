import sys
from tracemalloc import start

read = sys.stdin.readline

N, M = map(int, read().split())
nums = list(map(int, read().split()))
sum_nums = [0] * (1+N)
sum_nums[1] = nums[0]
for i in range(1,N):
    sum_nums[i+1] = sum_nums[i] + nums[i]

for j in range(M):
    s, e = map(int, read().split())
    print(sum_nums[e]-sum_nums[s-1])
