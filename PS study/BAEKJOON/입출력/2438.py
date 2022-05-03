import sys

read = sys.stdin.readline
count = int(read())
s= ""

for i in range(count):
    s = s + "*"*(i+1)+"\n"

print(s)