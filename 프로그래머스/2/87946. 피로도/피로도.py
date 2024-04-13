from itertools import permutations

def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    l = list(permutations(range(N),N))
    
    for order in l:
        remain = k
        count = 0
        for i in range(N):
            if dungeons[order[i]][0] <= remain:
                remain -= dungeons[order[i]][1]
                count += 1
                # print(order,"Clear",order[i],"dungeons and reamin is",remain, "count is", count)
            if N-i+count < answer:
                break
        answer = max(answer, count)
        
    
    return answer