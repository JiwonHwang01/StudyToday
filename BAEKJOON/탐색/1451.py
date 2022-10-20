import sys

def sum_double_array(arr, x1, x2, y1, y2):
    sum = 0
    for i in range(y1,y2):
        for j in range(x1,x2):
            sum += arr[i][j]
    
    return sum

read = sys.stdin.readline

n, m = map(int,read().split())
arr = [[0]*m for _ in range(n)]
sum = 0
for i in range(n):
    line = read()
    for j in range(m):
        arr[i][j] = int(line[j])
        sum += int(line[j])

res = 0
for i in range(0,n):
    for j in range(0,m):
        a, b, c = 0, 0, 0

        if i < n-1 and j < m-1:
            a = sum_double_array(arr,0,j,0,i)
            b = sum_double_array(arr,j,m,0,i)
            c = sum_double_array(arr,0,j,i,n)
            if b >= c : c += sum_double_array(arr,j,m,i,n)
            else : b += sum_double_array(arr,j,m,i,n)
            if res < a*b*c:
                    res = a*b*c
                
        elif j == m-1:
            a = sum_double_array(arr,0,m,0,i)
            for k in range(0, m):
                b = sum_double_array(arr,0,k,i,n) 
                c = sum_double_array(arr,k,m,i,n)
                if res < a*b*c:
                    res = a*b*c
            
            for l in range(i+1, n):
                b = sum_double_array(arr,0,m,i,l)
                c = sum_double_array(arr,0,m,l,n)
                if res < a*b*c:
                    res = a*b*c
            
        elif i == n-1:    
            a = sum_double_array(arr,0,j,0,n)
            for k in range(j+1, m):
                b = sum_double_array(arr,j,k,0,n) 
                c = sum_double_array(arr,k,m,0,n)
                if res < a*b*c:
                    res = a*b*c
            
            for l in range(0, n):
                b = sum_double_array(arr,j,m,0,l)
                c = sum_double_array(arr,j,m,l,n)
                if res < a*b*c:
                    res = a*b*c
print(res)
