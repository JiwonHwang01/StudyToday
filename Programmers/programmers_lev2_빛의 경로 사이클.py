def solution(grid):
    answer = []
    m, n = len(grid), len(grid[0])
    # 3차원 배열
    check = [[[False]*4 for _ in range(m)] for _ in range(n)]
    # 우하좌상
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    # x, y, dir
    pos = [0,0,0] 
    
    for i in range(m): #y
        for j in range(n): #x
            for k in range(4): #dir
                pos = [j, i, k]
                count = 0
                while True:
                    
                    #print("While(pos):",pos, count)
                    if check[pos[0]][pos[1]][pos[2]]:
                        if pos[0] == j and pos[1] == i and pos[2] == k and count:
                            #print("here")
                            answer.append(count)
                        #print("break")
                        break
                    check[pos[0]][pos[1]][pos[2]] = True
                    nx = (pos[0] + dx[pos[2]])%n
                    ny = (pos[1] + dy[pos[2]])%m
                    
                    if grid[ny][nx] == 'S':
                        pass
                    elif grid[ny][nx] == 'R':
                        pos[2] = (pos[2] + 1)%4
                    else: # 'L'
                        pos[2] = (pos[2] - 1)%4
                    
                    pos[0], pos[1] = nx, ny
                    count+=1
    answer.sort()
    return answer