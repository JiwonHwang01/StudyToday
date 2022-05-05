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
    
    ```python
    graph = [ # index 0번은 비움
    	[],
    	[2, 3, 8],
    	[1, 7],
    	[1, 4, 5],
    	[3, 5],
    	[3, 4],
    	[7],
    	[2, 6, 8],
    	[1, 7]
    ]
    
    visited = [False] * 9
    	
    
    def dfs(graph, v, visited):
    	visited[v] = True
    	
    	print(v, end= ' ')
    	for i in graph[v]:
    		if not visited[i]:
    			dfs(graph, i, visited)
    ```
    

### BFS

- queue를 사용
- 최단경로 문제에도 효과적으로 사용
    
    ```python
    from collections import deque
    
    graph = [ # index 0번은 비움
    	[],
    	[2, 3, 8],
    	[1, 7],
    	[1, 4, 5],
    	[3, 5],
    	[3, 4],
    	[7],
    	[2, 6, 8],
    	[1, 7]
    ]
    
    visited = [False] * 9
    
    def bfs(graph, start, visited):
    	queue = deque([start])
    	# 현재 노드를 방문 처리
    	visited[start] = True
    	
    	while queue:
    		# queue에서 하나씩 출력
    		v = queue.popleft()
    		print(v, end= ' ')
    		# 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    		for i in graph[v]:
    			if not visited[i]:
    				queue.append(i)
    				visited[i] = True
    
    bfs(graph, 1, visited)
    ```
