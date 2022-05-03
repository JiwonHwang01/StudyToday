import sys

read = sys.stdin.readline
s= ""
count = int(read())

for i in range(count):
    s += " "*(count-i-1) + "*"*(2*i+1)
    s += "\n"

print(s)