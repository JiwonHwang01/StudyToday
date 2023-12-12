def solution(triangle):
    answer = 0
    length = len(triangle[-1])-1
    
    for i in range(length):
        for j in range(length-i):
            triangle[length-i-1][j] += max(triangle[length-i][j],triangle[length-i][j+1])            
    
    answer = triangle[0][0]
    return answer