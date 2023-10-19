from itertools import combinations_with_replacement

def p(n, k):
    combs = list(combinations_with_replacement([i for i in range(k)],n-k))

    res = []
    for comb in combs:
        base = [1 for _ in range(k)]
        for c in comb:
            base[c] += 1
        res.append(base)
    
    return res

def consult(mt, stds):
    mts = [0] * mt
    res = 0
    
    for std in stds:
        mts.sort()
        if mts[0] == 0:
            mts[0] = std[0]+std[1]
            continue
        if mts[0] >= std[0]:
            res += mts[0] - std[0]
            mts[0] += std[1]
        else:
            mts[0] = std[0]+std[1]
    return res
        
    

def solution(k, n, reqs):
    answer = 1e9
    # 가능한 mento 조합 구하기
    mentos = p(n,k)
    # 학생 group화
    students = [[] for _ in range(k)]
    for req in reqs:
        students[req[2]-1].append(req[:2])
    
    # 완전 탐색
    for mento in mentos:
        tmp = 0
        for i in range(k):
            a= consult(mento[i],students[i])
            tmp += a
        answer = min(answer, tmp)
    
    return answer