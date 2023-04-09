import sys

e, s, m = map(int,sys.stdin.readline().split())
count = 0

for i in range(7980):
    e += 1
    s += 1
    m += 1
    if e > 15:
        e -= 15
    if s > 28:
        s -= 28
    if m > 19:
        m -= 19
    count += 1
    if count == 7980:
        count = 0
    if e == 15 and s == 28 and m == 19:
        print(7980 - count)
        break
