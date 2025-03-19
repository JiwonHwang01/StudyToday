import sys

read = sys.stdin.readline

N, M = map(int, read().split())

not_heard = [''] * N
not_saw = [''] * M

for i in range(N):
    not_heard[i] = read().rstrip()

for i in range(M):
    not_saw[i] = read().rstrip()

not_heard_not_saw = list(set(not_heard) & set(not_saw))
not_heard_not_saw.sort()
print(len(not_heard_not_saw))
print(*not_heard_not_saw, sep='\n')

