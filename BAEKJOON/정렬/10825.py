import sys

read = sys.stdin.readline

count = int(read())

data = [list(read().split()) for _ in range(count)]

data.sort(key = lambda x:(-int(x[1]),int(x[2]), -int(x[3]),x[0]))

name, _, _, _ = zip(*data)
print(*name,sep = '\n')
