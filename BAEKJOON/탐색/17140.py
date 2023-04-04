R, C, K = map(int,input().split())

A = [[0] * 100 for _ in range(100)]

for i in range(3):
    A[i][0], A[i][1], A[i][2] = map(int,input().rstrip().split())
row_cnt, cul_cnt = 3, 3
res = -1

def row_sort(Arr, row_cnt, cul_cnt):
    dic = dict()
    max_cnt = 0

    for i in range(row_cnt):
        for j in range(1,101):
            dic[j] = 0
        tmp = []
        for j in range(cul_cnt):
            if Arr[j][i]:
                dic[Arr[j][i]] += 1
        sorted_dic = sorted(dic.items(), key = lambda x:(x[1], x[0]))

        for (key, value) in sorted_dic:
            if len(tmp) > 100:
                break
            if not value:
                continue
            tmp.extend([key,value])

        for j in range(100):
            if j < len(tmp):
                Arr[j][i] = tmp[j]
                continue
            Arr[j][i] = 0

        if max_cnt < len(tmp):
            max_cnt = len(tmp)

    return Arr, max_cnt

def cul_sort(Arr, cul_cnt, row_cnt):
    dic = dict()
    max_cnt = 0

    for i in range(cul_cnt):
        for j in range(1,101):
            dic[j] = 0
        tmp = []
        for j in range(row_cnt):
            if Arr[i][j]:
                dic[Arr[i][j]] += 1
        sorted_dic = sorted(dic.items(), key = lambda x:(x[1], x[0]))
        for (key, value) in sorted_dic:
            if len(tmp) > 100:
                break
            if not value:
                continue
            tmp.extend([key,value])

        for j in range(100):
            if j < len(tmp):
                Arr[i][j] = tmp[j]
                continue
            Arr[i][j] = 0

        if max_cnt < len(tmp):
            max_cnt = len(tmp)
    
    return Arr, max_cnt

for time in range(101):
    if A[R-1][C-1] == K:
        res = time
        break
    
    if cul_cnt >= row_cnt:
        A, row_cnt = cul_sort(A,cul_cnt, row_cnt)
    else:
        A, cul_cnt = row_sort(A,row_cnt, cul_cnt)
print(res)