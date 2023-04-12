import sys
read = sys.stdin.readline
number = []
while True:
    n = int(read())
    if n == 0:
        break
    number.append(n)

p = [True] * (max(number)+1)

for i in range(4, len(p)):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            p[i] = False
            break

for i in number:
    for j in range(3, i, 2):
        if p[j] and p[i - j]:
            print("{} = {} + {}".format(i, j, i-j))
            break
        if j > i//2:
            print("Goldbach's conjecture is wrong.")
            break