## 자료구조 in Python
#### 스택

- 스택은 Python의 list를 그대로 사용하면된다
- push는 list.append()를 사용하고, pop은 list.pop()을 사용한다

#### 큐

- 큐는 `from collections import deque` 로 모듈을 추가하고,
    
    `queue = deque()` 로 선언한 후에 사용하면 된다
    
- queue.append()와 queue.popleft() 메소드를 이용한다

#### 힙

- 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
- 최소 힙과 최대 힙이 있다
- 리스트와 비교하면 삽입 시간은 O(1)과 O(logN)으로 더 오래 걸리지만,
    
    삭제 시간은 O(N)과 O(logN)으로 덜 걸린다.
    

**최소 힙**

heapq 라이브러리를 사용해 heap에 push 하기만 하면 구현 가능

**최대 힙**

```python
import heapq

def heapsort(iterable):
	h = []
	result = []
	for value in iterable:
		heapq.heappush(h,-value)
	for i in range(len(h)):
		result.append(heapq.heappop(h))

	return result
```