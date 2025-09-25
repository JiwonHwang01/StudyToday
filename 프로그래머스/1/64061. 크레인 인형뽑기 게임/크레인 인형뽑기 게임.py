def solution(board, moves):
    N = len(board)
    board = list(map(list,zip(*board)))
    stack = []
    answer = 0
#    print(board)
    for m in moves:
#        print('m:', m)
        for i in range(N):
            if board[m-1][i] != 0:
                tmp = board[m-1][i]
                board[m-1][i] = 0
                
                if len(stack)>0:
                    if stack[-1] == tmp:
                        stack.pop()
                        answer += 1
                        break
                                   
                stack.append(tmp)
                break
#        print('stack:', stack)
#    print(stack)
    
    return answer*2