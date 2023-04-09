n = int(input())

table = [True] * (n+1)
table[0] = False
table[1] = False
pNum = []

for i in range(2,int(n**0.5)+1):
    if table[i] == True:
        for j in range(i+i,n+1,i):
            table[j] = False

for i in range(2, n+1):
    if table[i]:
        pNum.append(i)

start = 0
count = 0
temp = 0

if n in pNum:
    count = 1

while True:
    if start > len(pNum) - 1:
        break
    if pNum[start] >= n/2:
        break

    for i in range(start, len(pNum)-1):
        if temp == n:
            count += 1
            start += 1
            temp = 0
            break


        elif temp > n:
            start += 1
            temp = 0
            break

        temp += pNum[i]





print(count)
