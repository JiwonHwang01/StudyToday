import sys
from collections import deque

read = sys.stdin.readline

def AC():
    p = read().rstrip()
    n = int(read())
    reverse = False

    if n == 0:
        number = []
        read()
    else :
        number = deque(map(int,read()[1:-2].split(",")))
    
    for command in p:
        if command =='R':
            reverse = not reverse
        else:
            if len(number) == 0:
                print("error")
                return
            if reverse:
                number.pop()
            else:
                number.popleft()

    if reverse:
        number = list(number)[::-1]
    else:
        number = list(number)
    print("[",end ='')
    print(*number, sep=',',end='')
    print("]")



t = int(read())

for _ in range(t):
    AC()
