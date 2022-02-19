import sys

read = sys.stdin.readline
count = int(read())

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    
    return a;

def lcm(a,b):
    return a * b // gcd(a,b)

for i in range(count):
    num1, num2 = list(map(int,read().split()))
    print(lcm(num1,num2))
