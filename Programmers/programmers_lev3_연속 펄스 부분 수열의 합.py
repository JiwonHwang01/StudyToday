def solution(sequence):
    answer = 0
    pulse_seq = [sequence[i]*((-1)**i) for i in range(len(sequence))]
    partial_sum = [0]*len(sequence)
    partial_sum[0] = pulse_seq[0]
    
    for i in range(1, len(pulse_seq)):
        partial_sum[i] = partial_sum[i-1] + pulse_seq[i] 
    partial_sum = [0]+partial_sum #이 줄을 놓쳐서 오답
    answer = max(partial_sum)-min(partial_sum)
    #print(partial_sum)
    
    
    return answer