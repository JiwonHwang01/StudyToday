import sys

read = sys.stdin.readline

str = read()
s = ""

for alpha in str:
    if ord(alpha)>=65 and ord(alpha)<=90 :
        s += chr(((ord(alpha)-65+13) % 26)+65)
    elif ord(alpha)>=97 and ord(alpha)<=122 :
        s += chr(((ord(alpha)-97+13) % 26) + 97)
    else :
        s += alpha

print(s)