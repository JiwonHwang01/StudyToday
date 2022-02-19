import sys

read = sys.stdin.readline

def gcd(a, b):
    if b ==0:
        return a
    return gcd(b, a%b)
    
    return a;

num1, num2 = list(map(int,read().split()))
print("1"*gcd(num1,num2))
