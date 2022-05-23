import sys
from bisect import bisect_left, bisect_right

read = sys.stdin.readline
n = int(read())
n_list = list(map(int,read().split()))
m = int(read())
m_list = list(map(int,read().split()))
n_list.sort()

for i in range(m):
    m_list[i] = bisect_right(n_list, m_list[i]) -bisect_left(n_list, m_list[i])

print(*m_list, sep = ' ')
    


