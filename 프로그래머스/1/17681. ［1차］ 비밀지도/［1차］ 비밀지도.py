def to_deci(n, length):
    res = ""
    while n > 0:
        res = str(n%2) + res
        n = n // 2
    res = "0"*(length-len(res)) + res
    return res
        
def solution(n, arr1, arr2):
    answer = [[0]*n for _ in range(n)]
    darr1 = [[] for _ in range(n)]
    darr2 = [[] for _ in range(n)]
    
    for i in range(n):
        darr1[i] = to_deci(arr1[i],n)
        darr2[i] = to_deci(arr2[i],n)
    
        answer[i] = "".join(['#' if (int(darr1[i][j]) or int(darr2[i][j])) else " " for j in range(n)])
        
    #print(darr1)
    #print(darr2)
    #print(answer)
    return answer