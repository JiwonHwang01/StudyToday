from lib2to3.pygram import python_grammar_no_print_statement
import sys

n = int(sys.stdin.readline())
start , end = 0,1
count = 0
prime = [True] * (n+1)

# 에라토스테네스의 체
for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i+i,n,i):
            prime[j] = False
prime_list = [i for i, j in enumerate(prime) if j == True and i >= 2]

sum_prime = [0] * (len(prime_list) + 1) 
for i in range(len(prime_list)):
    sum_prime[i+1] = sum_prime[i] + prime_list[i]

for i in range(len(sum_prime)):
    if start > len(sum_prime) or prime_list[end-1] > n:
        break
    if sum_prime[end] - sum_prime[start] == n:
        count += 1
        start += 1
    elif sum_prime[end] - sum_prime[start] > n:
        start += 1
    else:
        if end < len(sum_prime) - 1:
            end += 1
        else :
            start += 1


print(count)