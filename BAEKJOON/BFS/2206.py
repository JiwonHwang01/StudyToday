#벽 부수고 이동하기 #BFS
from collections import deque
def bfs():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append((0, 0, 1))
    visited[0][0][1] = 1
    while q:
        x, y, flag = q.popleft()
        
        if x == M-1 and y == N-1:
            return visited[y][x][flag]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if board[ny][nx] == '1' and flag == 1:
                    visited[ny][nx][0] = visited[y][x][flag] + 1
                    q.append((nx,ny,0))
                elif board[ny][nx] == '0' and visited[ny][nx][flag] == 0:
                    visited[ny][nx][flag] = visited[y][x][flag] + 1
                    q.append((nx,ny,flag))
    return -1



    

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    print(bfs())
    #print(visited)