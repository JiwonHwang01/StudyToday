import sys

read = sys.stdin.readline
count = int(read())
stack = []
for _ in range(count):
    command = list(read().split())
    res = -1
    if command [0] == "push":
        stack.append(command[1])
        continue
    elif command [0] == "size":
        res = len(stack)
        
    elif command [0] == "pop":
        if len(stack) != 0 :
            res = stack.pop()

    elif command [0] == "empty":
        if len(stack) == 0:
            res = 1
        else : res = 0
        
    else: # top
        if len(stack) != 0 :
            res = stack[-1]

    print(res)