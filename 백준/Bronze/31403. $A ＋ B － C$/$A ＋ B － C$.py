import sys

read = sys.stdin.readline

A = read().rstrip()
B = read().rstrip()
C = read().rstrip()

print(int(A)+int(B)-int(C))
print(int(A+B)-int(C))
