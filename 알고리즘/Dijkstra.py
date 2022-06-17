import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF]  (n+1)

# 간선 정보 입력 받기
for _ in range(m)
	a, b, c = map(int, input(splite))
	# a to b, cost is c
	graph[a].append((b,c))

def dijkstra(start)
	q = []
	
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q # 큐가 비어있지 않다면
		
		dist, now = heapq.heappop(q)
		if distance[now]  dist # 이미 처리된 노드 탈출
			continue
		for i in graph[now]
			cost = dost + i[1]
			if cost  distance[i[0]]
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)