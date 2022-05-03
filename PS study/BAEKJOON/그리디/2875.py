import sys

n, m, k = map(int,sys.stdin.readline().split())
team_count = 0

def counting(n, m, k):
    if n < 2 or m < 1:
        return 0

    if n >= 2 * m:
        team_count = m
        n -= 2*m
        m = 0
    else:
        team_count = n // 2
        n -= 2 * team_count
        m -= team_count
    
    while n+m < k:
            team_count -= 1
            n += 2
            m += 1

    return team_count

team_count = counting(n,m,k)

print(team_count)
