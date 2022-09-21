n = int(input())

cnt = 0
row = [0] * n

def check(num):
    for i in range(num):
        if row[num] == row[i] or abs(row[num] - row[i]) == abs(num - i):
            return False
    
    return True

def dfs(num):
    global cnt

    if num == n:
        cnt += 1
        return
    
    for i in range(n):
        row[num] = i

        if check(num):
            dfs(num+1)     
 
dfs(0)
print(cnt)