import sys

read = sys.stdin.readline

channel = read()
btn_count = int(read())
btn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if btn_count != 0 : 
    err_btn = list(read().split())
    for err_num in err_btn:
        btn.remove(err_num)
result = 0
res_number = ""

def num_in_btn_check(buttons, chan):
    for digit in str(chan):
        if digit not in buttons:
            return False
    
    return True

result = abs(int(channel)-100)
min = 1000000
for i in range(999999):
    if abs(int(channel)-i) < min :
        if num_in_btn_check(btn, i):
            res_number = str(i)
            min = abs(int(channel)-i)
            tmp = len(res_number) + abs(int(channel)-int(res_number))
            if result > tmp:
                result = tmp

print(result)
