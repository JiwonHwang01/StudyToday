from math import factorial
import sys

read = sys.stdin.readline

num = int(read())
num = str(factorial(num))[::-1]

for alpha in num:
    if alpha != "0":
        print(num.index(alpha))
        break;
