from collections import deque
def traverse(graph, a, b):
    start = [a, b]
    count = [0, 0]
    
    for i in range(2):
        visited = [False] * (len(graph)+1)
        visited[0] = True
        q = deque()
        q.append(start[i])
        while q:
            node = q.popleft()
            visited[node] = True
            count[i] += 1
            
            for n in graph[node]:
                if not visited[n]:
                    q.append(n)
    
    return max(count)-min(count)
        
        
def solution(n, wires):
    answer = []
    wires.sort(key=lambda x:x[0])
    graph = [[] for _ in range(n+1)]
    k = len(wires)
    a, b = 0, 0
    try:
        for i in range(k):
            graph = [[] for _ in range(n+1)]
            for j in range(k):
                if j == i:
                    a, b = wires[j]
                    continue
                graph[wires[j][0]].append(wires[j][1])
                graph[wires[j][1]].append(wires[j][0])
            answer.append(traverse(graph, a, b))
            
        
    except:
        print("error")
    #print(answer)
    
    return min(answer)