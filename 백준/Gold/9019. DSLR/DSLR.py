#DSLR
from collections import deque

def dslr(i, num):
    if i == 0:
        return 2*num % 10000
    elif i == 1:
        return (num-1) % 10000
    elif i == 2: 
        return num // 1000 + (num % 1000)*10
    else:
        return (num // 10) + (num % 10)*1000

def bfs():
    global res
    q = deque()
    
    visit = ['']*10000
    q.append((A))

    while q:
        num = q.popleft()
        if num == B:
            res = visit[num]
            break
        
        for i in range(4):
            if num == 0 and i==0:
                continue
            dnum = dslr(i, num)
            
            if visit[dnum] == '':
                visit[dnum] = visit[num] + tag[i]
                q.append(dnum)




if __name__ == "__main__":
    T = int(input())
    tag = {0:'D', 1:'S', 2:'L', 3:'R'}
    
    for _ in range(T):
        A, B = map(int,input().split())
        res = -1
        bfs()
        print(res)