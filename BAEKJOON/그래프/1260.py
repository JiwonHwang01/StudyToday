import sys

read = sys.stdin.readline

n, m, v = map(int, read().split())
graph = []

for _ in range(m):
    graph.append(list(map(int,read().split())))