import math
from operator import is_
import sys
import time

read = sys.stdin.readlines

number = list(map(int,read()))

def is_prime(num):
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False 
    
    return True

for i in number:
    for j in range(3, i, 2):
        if is_prime(j) and is_prime(i - j):
            print("{} = {} + {}".format(i, j, i-j))
            break
        if j > i//2:
            print("Goldbach's conjecture is wrong.")
            break;