import sys

read = sys.stdin.readline

a, b, c, d = map(str,read().split())

num1 = int(a+b)
num2 = int(c+d)

print(num1+num2)