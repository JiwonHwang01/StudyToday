def solution(lottos, win_nums):
    answer = []
    grade = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    zeros = 0
    scores = 0
    for k in lottos:
        if k == 0:
            zeros += 1
        if k in win_nums:
            scores += 1
    answer = [grade[scores+zeros], grade[scores]]
    return answer