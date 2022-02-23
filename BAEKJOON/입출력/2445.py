import sys

read = sys.stdin.readline
count = int(read())
s = [""]*(2*count-1)

for i in range(count):
    s[i] = "*"*(i+1) + " "*2*(count-i-1) + "*"*(i+1)
for i in range(count-1):
    s[count+i] = s[count-i-2]
print(*s,sep="\n")