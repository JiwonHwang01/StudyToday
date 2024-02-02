from operator import xor

def solution(data, col, row_begin, row_end):
    answer = 0
    s_list = []
    
    data.sort(key=lambda x:(x[col-1],-x[0]))
    
    for i in range(row_begin, row_end+1):
        tmp = 0
        for j in range(len(data[i-1])):
            tmp += data[i-1][j]%i
        s_list.append(tmp)
    
    for i in range(row_end-row_begin+1):
        answer = xor(answer,s_list[i])
    
    return answer