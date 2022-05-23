import sys
from collections import deque

read = sys.stdin.readline

count = int(read())
d = deque()


for _ in range(count):
    command = list(read().split())

    if command[0] == 'push_back':
        d.append(int(command[1]))

    elif command[0] == 'push_front':
        d.appendleft(int(command[1]))

    elif command[0] == 'pop_front':
        if not len(d):
            print(-1)
        else:
            print(d.popleft())

    elif command[0] == 'pop_back':
        if not len(d):
            print(-1)
        else:
            print(d.pop())

    elif command[0] == 'size':
        print(len(d))

    elif command[0] == 'empty':
        print(int(len(d) == 0))

    elif command[0] == 'front':
        if not len(d):
            print(-1)
        else:
            print(d[0])

    else: # command 가 back일 경우
        if not len(d):
            print(-1)
        else:
            print(d[len(d)-1])
