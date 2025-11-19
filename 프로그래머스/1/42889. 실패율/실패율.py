from collections import Counter

def calculate(n, stages, counts):
    res = 0
    tmp = [counts[i] for i in set(stages) if i>=n]
    
    if not tmp:
        return 0
    
    return (counts[n]/sum(tmp))
    

def solution(N, stages):
    answer = []
    counts = Counter(stages)
    
    for i in range(1,N+1):
        answer.append((i, calculate(i, stages, counts)))
    answer.sort(key=lambda x:(-x[1],x[0]))

    res = []
    for i in range(len(answer)):
        res.append(answer[i][0])
    return res