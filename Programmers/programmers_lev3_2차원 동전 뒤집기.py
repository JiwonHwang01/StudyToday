import copy
def solution(beginning, target):
    answer = 0
    m, n = len(target), len(target[0])
    def cycle(arr1, arr2):
        res = 0
        
        for i in range(n):
            if arr1[0][i] != arr2[0][i]:
                for j in range(m):
                    arr1[j][i] = (arr1[j][i]+1)%2
                res+=1

        for i in range(m):
            if arr1[i][0] != arr2[i][0]:
                for j in range(n):
                    arr1[i][j] = (arr1[i][j]+1)%2
                res+=1

        for i in range(m):
            for j in range(n):
                if arr1[i][j] != arr2[i][j]:
                    return -1
        
        return res
    
    begin1 = copy.deepcopy(beginning)
    
    for i in range(n):
        beginning[0][i] = (beginning[0][i]+1)%2
    
    answer = min(cycle(begin1, target),1+cycle(beginning, target))
    
    return answer