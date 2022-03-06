import sys

read = sys.stdin.readlines

c = read()
a, b = map(int,c[0][:-1].split())
count = int(c[1][:-1])
num = [0] * count
deci = 0
s=  ""
for i in range(count):
    num = list(map(int,c[2][:-1].split()))

for i in range(len(num)):
    deci += num[i] * (a**(len(num)-1-i))

while deci > 0:
    s = str(deci % b) + " " + s
    deci = deci // b

print(s)