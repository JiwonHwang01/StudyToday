import sys
import time
t = int(sys.stdin.readline())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

list = [2,3]
for i in range(5,10000,2):
    if is_prime(i):
        list.append(i)

for _ in range(t):
    n = int(sys.stdin.readline())
    
    if n == 4:
        print("2 2")
        continue
    
    for i in range(int(n//2),0,-1):
        if i % 2 == 0:
            continue
        if i in list and n-i in list:
            num1, num2 = i, n-i
            break
    print(f"{num1} {num2}")
        
    