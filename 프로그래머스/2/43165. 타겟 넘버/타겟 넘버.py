def dfs(res, depth, numbers, target):
    if depth == len(numbers):
        if res == target:
            return 1
        else:
            return 0
    
    return dfs(res+numbers[depth], depth+1, numbers, target) + dfs(res-numbers[depth], depth+1, numbers, target)
    

def solution(numbers, target):
    
    return dfs(0,0,numbers, target)
    
