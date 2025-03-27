import sys

read = sys.stdin.readline
T = int(read())
fibo = [0] * 41
fibo[1] = 1

for _ in range(T):
    N = int(read())
    if N == 0:
        print("1 0")
        continue
    elif N == 1:
        print("0 1")
        continue
    for i in range(2, N+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    print(fibo[N-1], fibo[N])