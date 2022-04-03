import time
import sys

read = sys.stdin.readline
sum_time = 0
count = int(read())

time_list = list(map(int,read().split()))
start_time = time.time()

time_list.sort()
for i in range(count):
    sum_time += time_list[i]*(count-i)

print(sum_time)

end_time = time.time()
print(end_time- start_time)

