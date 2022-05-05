import sys
from collections import deque

read = sys.stdin.readline
count = int(read())
queue = deque()

for _ in range(count):
    command = list(read().split())
    res = -1
    if command [0] == "push":
        queue.append(command[1])
        continue

    elif command [0] == "size":
        res = len(queue)
        
    elif command [0] == "pop":
        if len(queue) != 0 :
            res = queue.popleft()

    elif command [0] == "empty":
        if len(queue) == 0:
            res = 1
        else : res = 0
    
    elif command [0] == "front":
        if len(queue) != 0:
            res = queue[0]
    
    else: # back
        if len(queue) != 0 :
            res = queue[-1]

    print(res)