from collections import deque

def solution(maps):
    answer = []
    M, N = len(maps[0]), len(maps)
    visited = [[False]*M for _ in range(N)]
    q = deque()
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    
    for i in range(N): # i는 세로, y(N)
        for j in range(M): # j는 가로, x(M)
            if visited[i][j] or maps[i][j] == 'X':
                continue
            else:
                q.append([j,i])
                count = int(maps[i][j])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<=nx<M and 0<=ny<N:
                            if not visited[ny][nx] and not maps[ny][nx]=='X':
                                q.append([nx,ny])
                                visited[ny][nx] = True
                                count += int(maps[ny][nx])
                answer.append(count)
                
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    
    
    #print(M,N,visited)
    
    return answer