def solution(name, yearning, photo):
    answer = []
    point = {man:i for man, i in zip(name, yearning)}
    for p in photo:
        sum = 0
        for ppl in p:
            try:
                sum += point[ppl]
            except:
                continue
        answer.append(sum)
    
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))