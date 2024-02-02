def solution(cards):
    answer = 0
    l = len(cards)
    visit = [False]*(l+1)
    
    group = []
    for i in range(l):
        tmp = []
        if visit[i+1]:
            continue
        k = cards[i]
        while not visit[k]:
            tmp.append(k)
            visit[k] = True
            k = cards[k-1]
        group.append(tmp)
    if len(group) > 1:
        group.sort(key=lambda x:-len(x))
        answer = len(group[0])*len(group[1])
            
    
    return answer