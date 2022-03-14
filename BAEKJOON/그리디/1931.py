import sys
import time

read = sys.stdin.readline

count = int(read())
start_time = time.time()
time_list = [[0,0] for _ in range(count)]
res_list = [-1, -1]
res = 0

for i in range(count):
    time_list[i] = list(map(int,read().split()))

time_list.sort(key =lambda x: x[0])

for times in time_list:
    print(times, res_list, res)
    if times[0] > res_list[1]:
        res_list = times
        res += 1 
        continue
    if times[1] < res_list[1]:
        res_list = times
    
print(res)




#print(time_list)
end_time=time.time()
print(end_time-start_time)