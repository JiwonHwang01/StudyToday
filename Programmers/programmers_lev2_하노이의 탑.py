def solution(n): 
    def hanoi(n,a,b):
        #answer
        # n개를 a에서 b로 옮기기
        if n == 1:
            return [[a,b]]
        
        return hanoi(n-1,a,6-a-b)+hanoi(1,a,b)+hanoi(n-1,6-a-b,b)
    
    return hanoi(n,1,3)