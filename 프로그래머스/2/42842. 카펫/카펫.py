def solution(brown, yellow):
    r = 1
    while True:
        c = brown//2 - 2 - r
        if r<c:
            r += 1
            continue
        if r * c == yellow:
            break
        r+=1
        
        
    answer = [r+2, c+2]
    return answer