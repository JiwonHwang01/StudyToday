import sys

def func(n):
    #res = 0
    if dp[n]>=0:
        return dp[n]
    if len(graph[n]) == 0:
        dp[n] = D[n-1]
        return D[n-1]
    res = 0
    for num in graph[n]:
        res = max(res, func(num)+D[n-1])
    dp[n] = res
    return res

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        D = list(map(int, input().split()))
        graph = [[] for _ in range(N+1)]
        for _ in range(K):
            x, y = map(int, input().split())
            graph[y].append(x)
        W = int(input())
        
        dp = [-1]*(N+1)
        func(W)
        print(dp[W])
        
