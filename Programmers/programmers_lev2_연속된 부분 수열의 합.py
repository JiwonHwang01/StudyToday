def solution(sequence, k):
    answer = []
    l = len(sequence)
    p_sum = [0]*l
    p_sum[0] = sequence[0]
    s, e = 0, 0
    
    for i in range(1,l):
        p_sum[i] = p_sum[i-1] + sequence[i]
    p_sum = [0] + p_sum
    
    while True:
        if s > e or e == len(p_sum):
            break
        tmp = p_sum[e] - p_sum[s]
        if tmp > k:
            s += 1
        elif tmp == k:
            answer.append([s,e-1])
            e += 1
        else:
            e += 1
    answer.sort(key = lambda x : (x[1]-x[0],x[0]))
    
    #print(p_sum)
    return answer[0]