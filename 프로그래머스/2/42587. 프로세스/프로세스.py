def solution(priorities, location):
    answer = 0
    order = sorted(priorities, reverse=True)
    p = list(enumerate(priorities))
    #print('start:',p)
    
    j = 0
     #중요도
    i = 1
    
    while True:
        pos = order[j]
        cur = p[0]
        if cur[1] == pos:
            if cur[0] == location:
                return i
            p = p[1:]
            j+=1
            i+=1
            #print(i,j)
            continue
        p = p[1:]+[p[0]]
        #print(p)
    
    
    return answer