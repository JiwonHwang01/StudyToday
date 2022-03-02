import sys

read = sys.stdin.readline

count = int(read())
s = ""

for i in range(count):
    s += " "*(count-i-1) + "*" + " *" *i + "\n"

print(s)