import copy

def dfs(b, depth):
    global res
    if depth == len(cctv_list):
        res = min(res, count_zero(b))

        return

    b_copy = copy.deepcopy(b)
    x, y, type = cctv_list[depth]

    for direc in cctv_direction[type]:
        cctv(x, y, direc, b_copy)
        dfs(b_copy, depth + 1)

        b_copy = copy.deepcopy(b) # 중요


def cctv(x, y, direc, b):
    for d in direc:
        nx = x
        ny = y
        while True:

            nx += dx[d]
            ny += dy[d]
            # print(x, y, d, nx, ny)
            if 0 <= nx < M and 0 <= ny < N:
                if b[ny][nx] == 6:
                    break
                elif b[ny][nx] == 0:
                    b[ny][nx] = '#'
            else:
                break

def count_zero(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv_list = []

res = int(1e9)
dx = [0 ,1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] < 6:
            cctv_list.append((j,i,board[i][j]))

cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[1, 3], [0, 2]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
dfs(board, 0)
print(res)