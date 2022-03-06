import sys

read = sys.stdin.readline

a, b = map(int, read().split())
s = ""
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(a, b+1):
    if is_prime(i):
        s += str(i) + "\n"

print(s)