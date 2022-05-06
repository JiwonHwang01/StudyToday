import sys

read = sys.stdin.readline
n = int(read())
card_have = list(map(int, read().split()))
m = int(read())
card_find = list(map(int, read().split()))
card_have.sort()
found = False
last_pos = 0
for i in range(m):
    start, end = 0, n-1
    
    if found:
        if card_find[i] < last_num:
            end = last_pos - 1
        elif card_find[i] > last_num:
            start = last_pos + 1

    found = False
    while end >= start :
        mid = (start + end) // 2
        if card_have[mid] == card_find[i]:
            last_pos, last_num = mid, card_find[i]
            card_find[i] = 1
            found = True
            break

        elif card_have[mid] < card_find[i]:
            start = mid + 1
            
        else :
            end = mid - 1
        
        
    if not found:
        last_pos, last_num = mid, card_find[i]
        card_find[i] = 0

print(*card_find, sep= ' ')