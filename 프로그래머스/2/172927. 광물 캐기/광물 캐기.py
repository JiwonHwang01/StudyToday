mat = {'diamond':2, 'iron':1, 'stone':0}
from math import ceil
def solution(picks, minerals):
    answer = 0
    minerals_int = []
    i = 0
    tmp = []
    if sum(picks)*5 < len(minerals):
        minerals = minerals[:sum(picks)*5]
    for mine in minerals:
        
        tmp.append(5**mat[mine])
        i += 1
        if i == 5:
            minerals_int.append(tmp)
            tmp = []
            i=0
    if len(tmp):
        minerals_int.append(tmp)
    minerals_int.sort(key=lambda x:-sum(x))
    print(minerals_int)
    
    pick_int = []
    for i in range(3):
        pick_int += [5**(2-i)]*picks[i]
    print(pick_int)
    
    for i in range(min(len(minerals_int),len(pick_int))):
        for item in minerals_int[i]:
            answer += ceil(item/pick_int[i])
    print(answer)
    return answer