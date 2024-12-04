def solution(sizes):
    N = len(sizes)
    lst1, lst2 = [0 for _ in range(N)], [0 for _ in range(N)]
    for i in range(N):
        lst1[i] = max(sizes[i])
        lst2[i] = min(sizes[i])
    
    return max(lst1)*max(lst2)