#BFS #구슬탈출
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0  
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    
    q.append((rx, ry, bx, by, 1))
    check[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0
    
    # 다음이 벽이거나 현재가 구멍일 때까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def main():
    pos_init()

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth > 10:
            break
        
        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, dx[i], dy[i])
            #print('move RED', rnx, rny)
            bnx, bny, bcnt = move(bx, by, dx[i], dy[i])
            #print('move BLUE', bnx, bny)
            if board[bnx][bny] != 'O':
                if board[rnx][rny] == 'O':
                    return depth
                
                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]
                    
                if not check[rnx][rny][bnx][bny]:
                    check[rnx][rny][bnx][bny] = True
                    q.append((rnx, rny, bnx, bny, depth+1))
    
    return -1

res = main()
print(res)