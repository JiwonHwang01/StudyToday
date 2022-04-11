import sys

read = sys.stdin.readline

n, m = map(int,read().split())
arr = [[0]*m for _ in range(n)]
sum = 0
for i in range(n):
    line = read()
    for j in range(m):
        arr[i][j] = int(line[j])
        sum += int(line[j])

avg = sum / (m*n)

for i in range(1,n):
    for j in range(1,m):
        a, b, c = 0
        if i < n and j < m :
            for k in range(0,i+1):
                for l in range(0,j+1):
                    a += arr[k][l]
            
            for k in range(i+1,n):
