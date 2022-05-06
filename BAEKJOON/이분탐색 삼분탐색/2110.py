import sys

read = sys.stdin.readline
n, c = map(int,read().split())
iptime = [int(read()) for _ in range(n)]

iptime.sort()
start, end = 0, n-1

while True:
    mid = ( start + end ) // 2
    
    tmp = min 