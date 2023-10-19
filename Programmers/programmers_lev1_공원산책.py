def find_pos(board, target):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == target:
                return j,i
    return -1,-1
    
def solution(park, routes):n
    size_y = len(park)
    size_x = len(park[0])
    pos_x, pos_y = find_pos(park, "S")
    direction = {"N":0, "S":1, "W":2, "E":3}
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for r in routes:
        flag = 0
        dir, count = r.split()
        dir = direction[dir]
        nx, ny = pos_x, pos_y
        for _ in range(int(count)):
            nx, ny = nx + dx[dir], ny + dy[dir]
            if nx<0 or nx>=size_x or ny<0 or ny>=size_y:
                flag = 1
                break

            if park[ny][nx] == "X":
                flag = 1
                break
        if not flag:
            pos_x, pos_y = nx, ny
    answer = [pos_y,pos_x]

    return answer

print(solution(["SOXOO","OOOOO","OOOOO", "OOOOO", "OOOOO"], ["E 3"]))