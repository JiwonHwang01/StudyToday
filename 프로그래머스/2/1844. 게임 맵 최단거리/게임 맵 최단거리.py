from collections import deque
def solution(maps):
    answer = 0
    #n이y, m이x
    n, m = len(maps), len(maps[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append([0,0,1])
    visited[0][0] = True
    
    while q:
        px, py, count = q.popleft()
        print(px, py, count)
        if px == m-1 and py == n-1:
            return count
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]
            
            if 0 <= nx < m and 0<= ny < n and maps[ny][nx] == 1:
                
                if not visited[ny][nx]:
                    #print("n", nx, ny, maps[ny][nx])
                    q.append([nx, ny, count+1])
                    visited[ny][nx] = True
        #print(q)
            
        
    
    
    
    return -1
