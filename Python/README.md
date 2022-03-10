# Algorithm with Python
> 파이썬 알고리즘에 도움 되는 내용들
## 시간 복잡도 
> 파이썬 기준 연산 횟수가 5억을 넘기면 일반적으로 5~15초 소요
* 실행 시간 계산해보기
```python
import time

start_time = time.time()

# Program code

end_time = time.time()
print(end_time - start_time) 
```

## List
* List comprehension
```python
# for문으로 홀수를 하나씩 append 하는 코드
list = []
for i in range(20):
    if i % 2 == 1 :
        list.append(i)

# list comprehension 사용한 코드
list = [ i for i in range(20) if i % 2 == 1]

## 알고리즘
#### 그리디
> 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법
   그리디 알고리즘은 정당성 판단이 중요하다
- **탐욕적 선택 속성(greedy choice property)**: 각 단계에서 탐욕적으로 내리는 선택이 항상 최적해로 가는 길 중 하나이다.
- **최적 부분 구조(optimal substructure)**: 부분 문제의 최적해에서 전체 문제의 최적해를 만들 수 있다.각 단계마다 어떻게 선택할 것인지 정해주어야 한다.
    
    ex ) 거스름돈 → 큰 단위(500)가 작은 단위들의 배수이므로 가능함