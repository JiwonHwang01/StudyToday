import time

from itertools import permutations
st_time = time.time()


for p in permutations(range(10),10):
    if p[0] != 0:
        continue
    #if p[0] > p[5]:
    #    continue
    #print(p)
end_time = time.time()
print(end_time-st_time)