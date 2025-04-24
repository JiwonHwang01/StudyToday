import sys
from collections import deque
read = sys.stdin.readline

a, b = map(int,read().split())
s = set()
q = deque()
q.append(b)
res = 0
flag = False
while q:
    k = q.popleft()
    if k == a:
        flag = True
        break

    if k % 2 == 0:
        q.append(k//2)
    elif str(k)[-1] == '1' and k != 1:
        q.append(int(str(k)[:-1]))
    else:
        break
    res += 1
    q = deque(set(q))

if flag:
    print(res+1)
else:
    print(-1)