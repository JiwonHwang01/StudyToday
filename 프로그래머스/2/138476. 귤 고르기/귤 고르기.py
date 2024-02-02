def solution(k, tangerine):
    answer = 0
    
    dic = {}
    
    for i in range(len(tangerine)):
        if tangerine[i] in dic:
            dic[tangerine[i]]+=1
        else:
            dic[tangerine[i]] = 1
    #print(dic)
    
    dic = sorted(dic.items(),key=lambda x:-x[1])
    #print(dic)
    
    idx = 0
    while k>0:
        k -= dic[idx][1]
        answer += 1
        idx+=1
    return answer