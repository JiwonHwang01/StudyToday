import sys
read = sys.stdin.readline

a, b, c = map(int,read().split())

def fun1(a, b):
    if b == 1:
        return a % c

    x = fun1(a, b//2)
    if b % 2 == 0:
        return (x ** 2) % c

    else:
        return (a * (x ** 2)) % c

print(fun1(a,b) % c)