import sys

read = sys.stdin.readline

sentence = read().rstrip()
find = read().rstrip()
e = len(find)
s = 0
res = 0
while True:
    if s+e > len(find) or len(find) > len(sentence):
        break
    flag = True
    for i in range(s,len(find)):
        if sentence[i] != find[i]:
            flag = False
            break
    if flag:
        res += 1
        find = '0'*e + find
        s += e
    else:
        find = '0'+find
        s += 1
    
print(res)
