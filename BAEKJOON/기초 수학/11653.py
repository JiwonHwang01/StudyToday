import sys

read = sys.stdin.readline

num = int(read())

def fun1(num):
    s = ""
    i = 2
    if num == 1:
        return

    while num > 1 and i <= num:
        if num % i == 0:
            s += str(i) + "\n"
            num = num // i
        else:
            i += 1
    print(s.rstrip())

fun1(num)