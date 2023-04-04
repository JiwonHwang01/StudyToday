#브루트포스
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

up, down = -1, -1

for i in range(R):
    if arr[i][0] == -1:
        up = i
        down = i + 1
        break

def spread():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    tmp_arr = [[0] * C for _ in range(R)]
    
    
    for i in range(C):
        for j in range(R):
            if arr[j][i] > 4:
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    
                    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] > -1:
                        tmp_arr[nx][ny] += arr[j][i] // 5
                        tmp_arr[j][i] -= arr[j][i] // 5
    
    for i in range(C):
        for j in range(R):
            arr[j][i] += tmp_arr[j][i]

def clean_up():
    tmp = arr[up][-1]
    arr[up] = [arr[up][0]] + [0] + arr[up][1:-1]
    for i in range(up,0,-1):
        arr[i-1][C-1], tmp = tmp, arr[i-1][C-1] # 1, 2
    tmp2 = arr[0][0]
    arr[0] = arr[0][1:-1] + [tmp] + [arr[0][-1]]
    for i in range(1,up):
        arr[i][0], tmp2 = tmp2, arr[i][0]

def clean_down():
    tmp = arr[down][-1]
    arr[down] = [arr[down][0]] + [0] + arr[down][1:-1]
    for i in range(1+down, R): # 4, 5, 6
        arr[i][C-1], tmp = tmp, arr[i][C-1] 
    tmp2 = arr[R-1][0]
    arr[R-1] = arr[R-1][1:-1] + [tmp] + [arr[R-1][-1]]
    for i in range(R-2,down,-1):
        arr[i][0], tmp2 = tmp2, arr[i][0] # 5, 4

def main():
    res = 0
    for _ in range(T):
        spread()
        clean_up()
        clean_down()

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                res += arr[i][j]
    print(res)

main()
