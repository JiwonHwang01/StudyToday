import sys

read = sys.stdin.readline
s= ""
count = int(read())

for i in range(count):
    s += " "*i + "*"*(count-i)
    s += "\n"

print(s)