from collections import deque

def solution(n, computers):
    answer = 0
    q = deque()
    visited = [False]*n
    flag = False
    
    for i in range(n):
        if visited[i]:
            continue
        else:
            q.append(i)
            visited[i] = True
            answer +=1
        while q:
            node = q.popleft()
            
            for j in range(n):
                if computers[node][j] and not visited[j]:
                    q.append(j)
                    visited[j] = True

    
    
    return answer