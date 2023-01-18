# DFS / BFS

탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

대표적인 그래프 탐색 알고리즘

## Stack

- 선입후출 / 입구와 출구가 동일
- 코드 : list를 만들어서 append() / pop() 이용 : O(1)
    
    ```python
    stack = []
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()
    
    print(stack[::-1]) # 최상단 원소부터 출력 [1, 3, 2, 5]
    print(stack) # 최하단 원소부터 출력 [5, 2, 3, 1]
    ```
    

## Queue

- 선입선출 / 입구와 출구가 모두 뚫려 있음
- 코드 : 덱 라이브러리 사용 & append와 popleft 사용 : O(1)

```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 /deque([3, 7, 1, 4])
queue.reverse() # 역순으로 바꿈
print(queue) # 나중에 들어온 원소부터 출력 / deque([4, 1, 7, 3])
```

## 재귀함수

- 스택에서 재귀함수를 이용
- 자기 자신을 다시 호출하는 함수
- for 나 while 없이 반복 가능
- 문제풀이에 이용할 때에는 재귀 함수의 종료 조건을 반드시 명시
- 예시) factorial , 유클리드 호제법

## DFS

- 깊이 우선 탐색 , 그래프에서 깊은 부분(멀리 있는 부분)을  우선적으로 탐색
- 스택 자료구조 or 재귀함수 이용

```python

# DFS 메서드 정의
def dfs(graph, v, visited):
		# 현재 노드를 방문 처리
		visited[v] = True
		print(v, end=' ')
		# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
for i in graph[v]:
		if not visited[i]: # cf. if not 문법의 경우 조건이 false(boolean값)면 코드블럭 실행
				dfs(graph, i, visited) 
# ------------------------------------------------------------------------------
# 각 노드가 연결된 정보를 2차원 리스트로 표현
# 처음 list는 공백 -> index에서는 0번째부터 시작하기 때문에 헷갈림 방지
# 같은 이유로 (index 0을 사용하지 않기 위해) 크기를 한 개 더 크게 함
graph = [
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

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 결과
# 1 2 7 6 8 3 4 5 
```



## BFS

- 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘
- 큐 자료구조 , 특정 조건에서의 최단경로문제
- 이해한 대로의 과정을 거치지만 최종적으로는 1과 거리가 1인 노드, 2인 노드 , 3인노드…

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
		# Queue 구현을 위해 deque 라이브러리 사용
		queue = deque([start])
		# 현재 노드를 방문처리
		visited[start] = True
		# 큐가 빌 때까지 반복
		while queue:
			# 큐에서 하나 원소를 뽑아 출력
			v = queue.popleft()
			print(v, end=' ')
			# 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
			for i in graph[v]:
				if not visited[i]:
						queue.append(i)
						visited[i] = True
# --------------------------------------------------------
# 각 노드가 연결된 정보를 2차원 리스트로 표현
# 처음 list는 공백 -> index에서는 0번째부터 시작하기 때문에 헷갈림 방지
# 같은 이유로 (index 0을 사용하지 않기 위해) 크기를 한 개 더 크게 함
graph = [
		[],
		[2, 3, 8], # -> 1번 노드가 2,3,8 노드와 인접되어 있음.
		[1, 7],
		[1, 4, 5],
		[3, 5],
		[3, 4],
		[7],
		[2, 6, 8],
		[1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

# 결과
# 1 2 3 8 7 4 5 6 
```
