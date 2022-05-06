import sys

read = sys.stdin.readline
count = int(read())
lst = [0] * count

for i in range(count):
    lst[i] =  list(read().split())
lst.sort(key = lambda x :int(x[0]))

for pos in lst:
    print(pos[0],pos[1])