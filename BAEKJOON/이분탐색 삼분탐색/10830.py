# 10830 분할정복
from audioop import mul
import sys

read = sys.stdin.readline

n, b = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(n)]

def mul_matrix(U, V):
    n = len(U)
    resMatrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            tmpInt = 0
            for k in range(n):
                tmpInt += U[i][k]*V[k][j]
            resMatrix[i][j] = tmpInt % 1000

    return resMatrix

def fun1(A, b):
    n = len(A)
    if b == 1:
        for i in range(n):
            A[i] = list(map(lambda x: x % 1000,A[i]))
        return A
    
    tmp = fun1(A, b//2)
    if b % 2:
        return mul_matrix(mul_matrix(tmp, tmp), A)
    else:
        return mul_matrix(tmp, tmp)

res = fun1(matrix, b)

for i in range(n):
    print(*list(map(lambda x: x % 1000,res[i])),sep=' ')