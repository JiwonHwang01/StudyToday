import sys

read = sys.stdin.readline

N = int(read())
stack = []
def isEmpty(l):
    if len(l)==0:
        return True 
    return False

for i in range(N):
    line = read().split()
    c = int(line[0])
    if c == 1:
        stack.append(int(line[1]))
    elif c == 2:
        if isEmpty(stack):
            print(-1)
        else:
            print(stack.pop())
    elif c == 3:
        print(len(stack))
    elif c == 4:
        print(int(isEmpty(stack)))
    elif c == 5:
        if isEmpty(stack):
            print(-1)
        else:
            print(stack[-1])
            
    else:
        pass