def solution(N, number):
    answer = -1
    dp = [0]
    
    for i in range(1,9):
        p_set = set()
        p_set.add(int(str(N)*i))
        for j in range(1,i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    p_set.add(op1+op2)
                    p_set.add(op1-op2)
                    p_set.add(op1*op2)
                    if op2 != 0:
                        p_set.add(op1/op2)
        if number in p_set:
            answer = i
            break
        dp.append(p_set)
        
    
    return answer