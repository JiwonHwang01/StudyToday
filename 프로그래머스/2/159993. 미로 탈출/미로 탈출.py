from collections import deque

def solution(maps):
    q = deque()
    m, n = len(maps), len(maps[0]) # m이 
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visit = [[1e9]*n for _ in range(m)]
    l_flag = 0
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                q.append([i,j])
                visit[i][j] = 0
                break
        if q:
            break
            
    while q:
        pos_x, pos_y = q.popleft()
        
        for i in range(4):
            nx, ny = pos_x + dx[i], pos_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] > visit[pos_x][pos_y]+1:
                if maps[nx][ny] == 'X':
                    continue
                    
                if l_flag and maps[nx][ny] == 'E':
                    #print(visit)
                    return visit[pos_x][pos_y] + 1
                
                #print(visit[pos_x][pos_y],nx,ny)
                if maps[nx][ny] == 'L':
                    tmp = visit[pos_x][pos_y]+1
                    visit = [[1e9]*n for _ in range(m)]
                    visit[nx][ny] = tmp
                    q = deque()
                    q.append([nx,ny])
                    l_flag = 1
                    #print(visit)
                    break
                
                q.append([nx,ny])
                visit[nx][ny] = visit[pos_x][pos_y] + 1
                    
                
                    
    
    answer = -1
    return answer