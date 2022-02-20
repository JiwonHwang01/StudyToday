import sys

read = sys.stdin.readline
count = int(read())
s= ""

for i in range(count):
    s = s + "*"*(count-i)+"\n"

print(s)