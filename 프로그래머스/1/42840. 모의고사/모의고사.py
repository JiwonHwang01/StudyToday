def solution(answers):
    answer = []
    scores = [0, 0, 0]
    N = len(answers)
    supo =[
        [1,2,3,4,5] * (N//5+1),
        [2,1,2,3,2,4,2,5] * (N//8 + 1),
        [3,3,1,1,2,2,4,4,5,5] * (N// 10 + 1)
    ] 
    for i in range(N):
        if supo[0][i] == answers[i]:
            scores[0] += 1
        if supo[1][i] == answers[i]:
            scores[1] += 1
        if supo[2][i] == answers[i]:
            scores[2] += 1
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i+1)
        
    return answer