import sys

read = sys.stdin.readline
N, M = map(int, read().split())
pw = {}
for i in range(N):
    site, password = read().split()
    pw[site] = password
for j in range(M):
    site = read().rstrip()
    print(pw[site])