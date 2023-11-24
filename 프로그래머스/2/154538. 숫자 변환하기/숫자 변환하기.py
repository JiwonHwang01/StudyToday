def solution(x, y, n):
    answer = 0
    used = set()
    used.add(x)
    if x == y:
        return 0
    
    while True:
        add_lst = set()
        answer += 1
        for items in used:
            lst = [2*items, 3*items,items+n]
            
            for item in lst:
                if item == y:
                    return answer
                if item < y:
                    add_lst.add(item)
                    
        if len(add_lst-used) == 0:
            return -1
        used = used.union(add_lst)
        
    return answer