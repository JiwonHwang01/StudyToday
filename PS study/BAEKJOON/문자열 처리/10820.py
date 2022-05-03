import sys

a = sys.stdin.readlines()
count = [0, 0, 0, 0]

for i in a:
    
    for chr in i:
        if chr == " ":
            count[3] += 1
        elif ord(chr) >= 97 and ord(chr) <= 122:
            count[0] += 1
        elif ord(chr) >= 65 and ord(chr) <= 90:
            count[1] += 1
        elif ord(chr) >= 48 and ord(chr) <= 57:
            count[2] += 1
        else :
            break
    print(*count,sep=" ")
    count = [0, 0, 0, 0]
