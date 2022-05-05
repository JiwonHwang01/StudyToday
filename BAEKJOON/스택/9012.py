import sys

read = sys.stdin.readline
count = int(read())
def VPS():
    stack = []
    line = read()[:-1]
    res = "NO"
    
    for c in line:
        if c == "(":
            stack.append(c)
        else :
            try:
                stack.pop()
            except:
                return "NO"
                
    if len(stack) == 0:
        res = "YES"
    return res

for _ in range(count):
    print(VPS())