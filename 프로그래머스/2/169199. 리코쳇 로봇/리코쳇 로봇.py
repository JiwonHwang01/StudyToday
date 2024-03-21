from collections import deque

def solution(board):
    answer = 0
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    N, M = len(board), len(board[0])
    rx ,ry, gx, gy = -1, -1, -1, -1
    count = [[1e9]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = j, i
                count[i][j] = 0
                #board[i].replace('R', '.')
            if board[i][j] == 'G':
                gx, gy = j, i
                #board[i].replace('G', '.')
    
    q = deque()
    q.append([rx,ry,0])
    #print(board)
    
    while q:
        posx, posy, cnt = q.popleft()
        
        for i in range(4):
            nx, ny = posx, posy
            while True:
                nx, ny = nx + dx[i], ny + dy[i]
                
                if 0 <= nx < M and 0 <= ny < N:
                    if board[ny][nx]=='D':
                        if cnt+1 < count[ny-dy[i]][nx-dx[i]]:
                            q.append([nx-dx[i],ny-dy[i],cnt + 1])
                            count[ny-dy[i]][nx-dx[i]] = cnt + 1
                        
                        break
                
                else:
                    #print(ny-dy[i],nx-dx[i], count[ny-dy[i]][nx-dx[i]])
                    if cnt+1 < count[ny-dy[i]][nx-dx[i]]:
                        q.append([nx-dx[i],ny-dy[i],cnt + 1])
                        count[ny-dy[i]][nx-dx[i]] = cnt + 1
                    break
                    
                    
                
            #print(q)

    
    if count[gy][gx] == 1e9:
        return -1
    answer = count[gy][gx]
    
    
        
    
    return answer