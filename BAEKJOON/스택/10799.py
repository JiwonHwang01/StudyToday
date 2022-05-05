import sys

read = sys.stdin.readline

line = read()[:-1]
stack = []
count = 0

for i in range(len(line)):
    if line[i] == "(":
        stack.append(line[i])
    else :
        stack.pop()
        if line[i-1] == "(":
            count += len(stack)

        else: 
            count += 1
    
print(count)