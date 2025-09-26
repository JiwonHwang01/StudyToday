def solution(s):
    n = len(s)
    answer = n
    
    for step in range(1, n // 2 + 1):  # 압축 단위 1 ~ N//2
        compressed = ""
        prev = s[0:step]   # 초기 윈도우
        count = 1

        # step 간격으로 윈도우 이동
        for i in range(step, n, step):
            cur = s[i:i+step]
            if cur == prev:
                count += 1
            else:
                # 지금까지의 압축 결과 붙이기
                compressed += (str(count) + prev) if count > 1 else prev
                prev = cur
                count = 1
        
        # 마지막 덩어리 붙이기
        compressed += (str(count) + prev) if count > 1 else prev

        # 최소 길이 갱신
        answer = min(answer, len(compressed))

    return answer
