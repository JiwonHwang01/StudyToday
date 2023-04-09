from collections import deque

N, M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            q.append((i,j))
            board[i][j] = 0
        elif board[i][j] == 1:
            board[i][j] = -1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
print(board)
while q:
    y, x = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:

            if board[ny][nx] >= 0:

                if board[y][x] == 0:
                    board[ny][nx] = 1
                    q.append((ny, nx))
                    print("first",nx,ny)
                else:
                    print(nx, ny)
                    if board[ny][nx] == 0:
                        board[ny][nx] = board[y][x] + 1
                        q.append((ny, nx))
                    if board[ny][nx] > board[y][x] + 1:
                        board[ny][nx] = board[y][x] + 1
                    print(q)
print(board)