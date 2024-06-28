def solution(board):
    answer = 1
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    Os = []
    Xs = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                Os.append([i,j])
            elif board[i][j] == 'X':
                Xs.append([i,j])
    if len(Os) > len(Xs) + 1 or len(Os) < len(Xs):
        return 0      
    
    Oflag, Xflag = False, False
    for lst in list(map(list,zip(*Os))):
        if len(lst) < 3:
            break
        if lst.count(0) == 3 or lst.count(1) == 3 or lst.count(2) == 3:
            Oflag = True
    for lst in list(map(list,zip(*Xs))):
        if len(lst) < 3:
            break
        if lst.count(0) == 3 or lst.count(1) == 3 or lst.count(2) == 3:
            Xflag = True
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == 'O':
            Oflag = True
        elif board[1][1] == 'X':
            Xflag = True
    if board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] == 'O':
            Oflag = True
        elif board[1][1] == 'X':
            Xflag = True

    if Oflag == True:
        if Xflag== True:
            return 0
        if not (len(Os) -len(Xs)==1):
            return 0
    elif Xflag == True:
        if not len(Os)==len(Xs):
            return 0
        
    return answer