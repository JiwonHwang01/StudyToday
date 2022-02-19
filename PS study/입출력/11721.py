import sys

a = sys.stdin.read()

for i in range(0,len(a)):
    print(a[i],end="")
    if(i%10 == 9): print("")