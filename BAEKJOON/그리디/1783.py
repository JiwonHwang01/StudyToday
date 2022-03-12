from math import ceil
import sys

n, m = map(int,sys.stdin.readline().split())

#  array = [[0]* m for _ in range(n)]


def adventure(n,m):
    if n < 2:
        return 1
    if n < 3:
        return min(4, ceil(m/2))
    else:
        if m < 7:
            return min(4, m)
        else: return m - 2

count = adventure(n, m)
print(count)