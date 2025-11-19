def solution(n, lost, reserve):
    answer = 0
    std = [1]*(n+2)
    std[0],std[n+1] = 0, 0
    for i in range(1, n+1):
        if i in reserve:
            std[i] = 2
        if i in lost:
            std[i] -= 1
    #print(std)
    
    for i in range(1, n+1):
        if std[i] == 0:
            if std[i-1] > 1:
                std[i-1], std[i] = std[i-1] - 1, std[i] + 1
                continue
            if std[i+1] > 1:
                std[i], std[i+1] = std[i] + 1, std[i+1] - 1
    
    for i in range(1, n+1):
        if std[i] >= 1:
            answer += 1
    #print(std)
            
            
        
    
    return answer