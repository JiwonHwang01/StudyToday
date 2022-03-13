import sys
import time

read = sys.stdin.readline

count = int(read())
start = time.time()
time_list = [[0]]*count
res_list = [[0]]* count
result = 0

for i in range(count):
    time_list[i] = list(map(int,read().split()))

time_list.sort(key =lambda x: x[0])








end=time.time()
print(end-start)