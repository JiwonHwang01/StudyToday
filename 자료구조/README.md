## 자료구조 in Python
#### 스택

- 스택은 Python의 list를 그대로 사용하면된다
- push는 list.append()를 사용하고, pop은 list.pop()을 사용한다

#### 큐

- 큐는 `from collections import deque` 로 모듈을 추가하고,
    
    `queue = deque()` 로 선언한 후에 사용하면 된다
    
- queue.append()와 queue.popleft() 메소드를 이용한다
