import sys

read = sys.stdin.readlines

c = read()
count = int(c[0][:-1])
num = [0] * count
cnt = 0

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(count):
    num = list(map(int,c[1][:-1].split()))

for number in num:
    if number == 1 :
        continue
    if is_prime(number):
        cnt += 1

print(cnt)