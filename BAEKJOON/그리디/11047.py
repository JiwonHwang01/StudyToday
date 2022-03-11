import sys

read = sys.stdin

n, k = map(int,read.readline().split())
coins = [0] * n
count = 0

coins = list(map(int, read.readlines()))
coins.sort(reverse=True)

for coin in coins:
    if coin > k:
        continue
    
    count += k//coin
    k %= coin

print(count)
