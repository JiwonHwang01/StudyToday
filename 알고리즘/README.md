# Algorithm in Python

## 알고리즘
#### GCD, LCM
> 정리하자

#### 그리디
> 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법
> 
> 그리디 알고리즘은 정당성 판단이 중요하다
- **탐욕적 선택 속성(greedy choice property)**: 각 단계에서 탐욕적으로 내리는 선택이 항상 최적해로 가는 길 중 하나이다.
- **최적 부분 구조(optimal substructure)**: 부분 문제의 최적해에서 전체 문제의 최적해를 만들 수 있다.각 단계마다 어떻게 선택할 것인지 정해주어야 한다.
    
    ex ) 거스름돈 → 큰 단위(500)가 작은 단위들의 배수이므로 가능함

## DFS & BFS
> 예제는 이 문제로	
    <img width="441" alt="image" src="https://user-images.githubusercontent.com/72727113/166429856-20724253-bc37-40a4-ade1-1352ff601ea3.png">
### DFS

- stack과 recursion 사용
- [DFS 코드 보기](https://github.com/JiwonHwang01/StudyToday/edit/main/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/DFS.py)
    

### BFS

- queue를 사용
- 최단경로 문제에도 효과적으로 사용
- [BFS 코드 보기](https://github.com/JiwonHwang01/StudyToday/edit/main/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/BFS.py)

## 정렬
> 퀵이랑 계수 정렬만
### 퀵 정렬

- pivot 값을 첫번째 값으로 설정하고, 왼쪽부터 찾아서 pivot보다 큰수와 오른쪽부터 찾아서 pivot보다 작은값을 찾아서 바꾸는데,  큰 수가 작은 수보다 더 오른쪽에 있을때는 작은 수와 pivot 값을 바꾸고 왼쪽과 오른쪽에 대해서 recursion 수행
- 대부분의 경우에 적합하며, 충분히 빠름
- 시간 복잡도
    - 평균 O(Nlog(N)) 
    - 최악 O(N<sup>2</sup>)

> [파이썬 List Comprehension 을 사용해서 간단하게 구현](https://github.com/JiwonHwang01/StudyToday/edit/main/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/quickSort.py)


### 계수 정렬

- 데이터의 **범위가 제한**되어 정수로 표현할 수 있을 때 매우 빠름

```python
count = [0] * (max(array) + 1)

for i in range(len(array)):
		count[array[i]] += 1

for i in range(len(count)):
		for j in range(count[i]):
				print(count[i])
```

- 시간 복잡도 ( N개의 정수, K까지의 범위 )
    - O(N+K)

## 다익스트라
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
- 음의 간선이 없을 때 정상적으로 동작함
- 분류하자면 그리디 알고리즘으로 분류
    
    → 매 상황에서 가장 적은 비용의 노드를 선택
    

## 동작 과정

1. 출발 노드 설정
2. 최단 거리 테이블을 초기화
    1. 거치지 않은 노드의 값을 무한으로 수정함
3. 방문하지 않은 노드 중 최단거리 노드 선택
4. 해당 노드를 거쳐서 다른 노드로 가는 비용을 계산하여 테이블 갱신
    1. 비용이 노드의 현재값보다 작으면 갱신
    2. 갱신이 되는 노드를 우선순위 큐에 삽입 ( 우선순위큐는 비용으로 정렬 )
5. 3번과 4번의 반복

> <img width="306" alt="image" src="https://user-images.githubusercontent.com/72727113/174304460-71ccdd01-2472-4394-96fe-194a4efcd9ab.png">

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
	a, b, c = map(int, input(splite))
	# a to b, cost is c
	graph[a].append((b,c))

def dijkstra(start):
	q = []
	
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q: # 큐가 비어있지 않다면
		
		dist, now = heapq.heappop(q)
		if distance[now] < dist: # 이미 처리된 노드 탈출
			continue
		for i in graph[now]:
			cost = dost + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)
```