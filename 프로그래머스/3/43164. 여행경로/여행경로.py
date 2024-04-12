from collections import deque
def solution(tickets):
    answer = []
    tickets.sort(key = lambda x:(x[0],x[1]))
    N = len(tickets)
    checked = [False]*N
    print(tickets)
    def compare(city1, city2):
        for i in range(3):
            if city1[i] != city2[i]:
                return False
        return True
    
    def dfs(city, checked, depth, path):
        if depth == N:
            answer.append(path)
            return
        
        for i in range(N):
            if compare(city,tickets[i][0]) and not checked[i]:
                checked[i] = True
                #print(city, "TO", tickets[i][1])
                #print(depth, path)
                dfs(tickets[i][1], checked, depth + 1, path+[tickets[i][1]])
                checked[i] = False
        
    dfs("ICN", checked, 0, ["ICN"])
    return answer[0]