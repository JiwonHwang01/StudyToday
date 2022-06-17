import sys

read = sys.stdin.readline

string = read()[:-1]
count = int(read())
pos = len(string)

for _ in range(count):
    command = list(read().split())

    if command[0] == 'L':
        if pos:
            pos -= 1
        
    elif command[0] == 'D':
        if pos < len(string):
            pos += 1
        
    elif command[0] == 'B':
        if pos:
            string = string[:pos-1] + string[pos:]
            pos -= 1

    else:
        if pos:
            string = string[:pos] + command[1] + string[pos:]
        else:
            string = command[1] + string
        pos += 1

print(string)