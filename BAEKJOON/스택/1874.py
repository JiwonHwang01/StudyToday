t = int(input())
stack = []
res = ""
flag = 0
pStack = 1
for i in range(t):
    num = int(input())
    if flag == 1:
        continue
    while pStack <= num:
        stack.append(pStack)
        res += "+"
        pStack += 1

    if stack[-1] == num:    
        stack.pop()         
        res += "-"
    else:                   
        res = "NO"        
        flag = 1
                       

if flag == 0:
    print("\n".join(res))
else:
    print(res)