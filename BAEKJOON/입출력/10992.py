import sys

read = sys.stdin.readline

count = int(read())
s = ""

for i in range(count-1):
    if i == 0:
        s = " "*(count-i-1) + "*\n"
        continue
    s += " "*(count-i-1) + "*" + " " *(2*i-1) + "*\n"
s += "*"*(2*count -1)
print(s)