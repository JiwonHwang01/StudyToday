import sys
read = sys.stdin.readline

N = int(read())
li = []
order = {}
for i in range(N):
    command = read().rstrip().split()
    if command[1] == 'enter':
        order[command[0]] = 1
    else:
        order[command[0]] = 0

for key, value in order.items():
    if value == 1:
        li.append(key)
print(*sorted(li, reverse=True), sep='\n')