def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[1],x[0]))
    idx = routes[0][1]
    answer += 1
    for i in range(len(routes)):
        if routes[i][0] > idx:
            # print(i,routes[i][1])
            answer += 1
            idx = routes[i][1]
    
    return answer