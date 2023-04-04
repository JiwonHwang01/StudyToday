#postfix #stack
import sys

input = sys.stdin.readline
stack = []
operator = {'+':2, '-':2, '*':1, '/':1}
infix = list(input().rstrip())
res = ''

def isOper(char):
    if char in operator:
        return operator[char]
    if char in '()':
        return 3
    return 0

for i in range(len(infix)):
    ch = infix[i]
    num = isOper(ch)

    if num:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack:
                c = stack.pop()
                if c =='(':
                    break
                res += c
        else:
            while stack and isOper(stack[-1]) <= num:
                c = stack.pop()
                res += c
            stack.append(ch)
    else:
        stack.append(ch)

res += ''.join(stack[::-1])
print(res)