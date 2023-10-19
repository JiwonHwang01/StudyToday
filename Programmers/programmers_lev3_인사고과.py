def solution(scores):
    answer = -1
    target = scores[0][0] + scores[0][1]
    target_a, target_b = scores[0][0], scores[0][1]
    sum_scores = [-1]*len(scores)
    cut = 0
    
    if len(scores)==1:
        return 1
    
    scores.sort(key = lambda x:(-x[0],x[1]))
    
    for i in range(len(scores)):
        if i == 0:
            sum_scores[0] = scores[0][0] + scores[0][1]
            cut = scores[0][1]
            continue
        
        if scores[i][1] < cut:
            if scores[i][0] == target_a and scores[i][1] == target_b:
                return -1
            sum_scores[i] = -1
            continue
        cut = max(cut,scores[i][1])
        sum_scores[i] = scores[i][0] + scores[i][1]
    sum_scores.sort(reverse=True)
    #print(sum_scores)

    answer = sum_scores.index(target)+1
    return answer