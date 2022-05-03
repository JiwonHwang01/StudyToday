import sys

marco = list(map(int,sys.stdin.readline().strip()))
marco.sort(reverse=True)

def marco_func(marco):
    s= ""
    if sum(marco) % 3 != 0 or marco[len(marco)-1] != 0:
        return -1
    for num in marco:
        s += str(num)
    return int(s)


result = marco_func(marco)
print(result)