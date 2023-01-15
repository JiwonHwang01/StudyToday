import sys
from itertools import combinations

read = sys.stdin.readline

n, m = map(int, read().split())
city = [[0]*n for _ in range(n)]
store = []
res = int(10**9)

for i in range(n):
    row = list(map(int, read().split()))
    city[i] = row
    
    for j in range(n):
        if row[j] == 2:
            store.append((i,j))
            
comb = list(combinations(range(len(store)),m))

for k in range(len(comb)):
    chicken_cost = 0
    cost = [[0]*n for _ in range(n)]

    for l in comb[k]:
        loc = store[l]
        for i in range(n):
            for j in range(n):
                if city[i][j] == 1:
                    distance = abs(loc[0]-i) + abs(loc[1] - j)
                    
                    if cost[i][j] == 0 or cost[i][j] > distance:
                        cost[i][j] = distance
    
    for i in range(n):
        chicken_cost += sum(cost[i])

    res = min(res, chicken_cost)

print(res)           