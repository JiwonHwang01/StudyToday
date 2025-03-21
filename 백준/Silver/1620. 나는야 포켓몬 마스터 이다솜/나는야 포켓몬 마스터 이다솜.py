import sys
read = sys.stdin.readline
N, M = map(int, input().split())
dogam_num = {}
dogam_name = {}

for i in range(N):
    name = read().rstrip()
    dogam_num[i+1] = name
    dogam_name[name] = i+1
    
for i in range(M):
    command = read().rstrip()
    if command.isdigit():
        print(dogam_num[int(command)])
    else:
        print(dogam_name[command])