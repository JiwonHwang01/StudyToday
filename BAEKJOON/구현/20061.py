# 구현
N = int(input())
blue_board = [[0]*6 for _ in range(4)]
green_board = [[0]*4 for _ in range(6)]
res1, res2 = 0, 0

def search(board, x, y, lst):
    if board[y][x] == 1: 
        return lst
    lst.append(y)
    if y == 5:
        return lst
    
    return search(board, x, y+1, lst)

def block1(board, x):
    tmp = []
    tmp = search(board, x, 0, tmp)
    pos = tmp[-1]
    board[pos][x] = 1

    return board

def block2(board, x):
    tmp = []
    search(board, x, 0, tmp)
    
    for pos in tmp[::-1]:
        if board[pos-1][x] == 0:
            board[pos][x] = 1
            board[pos-1][x] = 1
            break
            
    return board
    
def block3(board, x):
    tmp = []
    search(board, x, 0, tmp)
    tmp2 = []
    search(board, x+1, 0, tmp2)
    pos = list(set(tmp).intersection(set(tmp2)))[-1]
    
    board[pos][x] = 1
    board[pos][x+1] = 1

    return board

def check(board):
    global res1
    cursor = 0
    while True:
        if cursor > 5:
            break
        if sum(board[cursor]) == 4:
            res1 += 1
            board = [[0, 0, 0, 0]] + board[:cursor] + board[cursor+1:]
        cursor += 1
    for i in range(2):
        if sum(board[i]) > 0:
            board = [[0, 0, 0, 0]] + board[:5]

    return board

def count(board):
    global res2

    for i in range(6):
        res2 += sum(board[i])

b_zip = list(map(list,zip(*blue_board)))
for _ in range(N):
    t, y, x = map(int, input().split())
    

    if t == 1:
        block1(b_zip, y)
        block1(green_board, x)
    elif t == 2:
        block2(b_zip, y)
        block3(green_board, x)
    else:
        block2(green_board, x)
        block3(b_zip, y)
    
    b_zip = check(b_zip)
    green_board = check(green_board)
    print(list(map(list,zip(*b_zip))))
    print(green_board)
count(b_zip)
count(green_board)

print(res1)
print(res2)