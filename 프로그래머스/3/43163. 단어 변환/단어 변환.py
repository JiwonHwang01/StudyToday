from collections import deque

def solution(begin, target, words):
    answer = 0
    def compare(w1, w2):
        l = len(w1)
        cnt = 0
        for i in range(l):
            if w1[i] != w2[i]:
                cnt += 1
        return cnt
            
        
    n = len(words)
    visited = [False] * n
    q = deque()
    q.append([begin,0])
    
        
    while q:
        now, count = q.popleft()
        # print([now, count])
        if compare(now,target) == 0:
            return count
        for i in range(n):
            # print(changable(now, words[i]))
            if not visited[i] and compare(now, words[i])==1:
                q.append([words[i],count+1])
                visited[i] = True
        
    
    
    return answer