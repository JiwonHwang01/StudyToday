#골드4 #유클리드호제법

n = int(input())
num_list = [0]*n
sub_list = [0]*(n-1)
res = []
prev = 0

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

for i in range(n):
    num_list[i] = int(input())

num_list.sort()

for i in range(n-1):
    sub_list[i] = num_list[i+1] - num_list[i]

prev = sub_list[0]

for i in range(1, n-1):
    prev = gcd(prev, sub_list[i])

res.append(prev)
for i in range(2, int(prev**0.5)+1):
    if prev % i == 0:
        res.append(i)
        res.append(int(prev//i))
        
print(res)
res = list(set(res))
res.sort()
print(*res,sep = " ")
