## DFS & BFS

- 대표적인 그래프 탐색 알고리즘
- 탐색(Search)이란 많은 양의 데이터중에서 원하는 데이터를 찾는 과


### 스택 자료구조

- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.


### 큐 자료구조

- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화할 수 있다.


### 재귀함수

- 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있다.
- 재귀 함수 사용의 유의 사항
	- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성가능.
	- 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 한다.
	- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
	- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
	- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
	- 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.

#### 최대공약수 계산 (유클리드 호제법) 예제

- 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로 유클리드 호제법이 있다.
- 유클리드 호제법
	- 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하자.
	- 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
	
	``` python
	def gcd(a, b):
	    if a % b == 0:
	        return b
	    else:
	        return gcd(b, a % b)
	```


### DFS (Depth-First Search)

- DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
- DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
	- 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
	- 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
	- 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
	
	``` python
	def dfs(graph, v, visited):
	    visited[v] = True
	    print(v, end=' ')
		
	    for i in graph[v]:
	        if not visited[i]:
	            dfs(graph, i, visited)
	```


### BFS (Breadth-First Search)

- BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다.
- BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다.
	- 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
	- 큐에서 노드를 꺼낸 뒤해 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
	- 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
	
	``` python
	from collections import deque

	def bfs(graph, start, visited):
	    queue = deque([start])
	    visited[start] = True

	    while queue:
                v = queue.popleft()
		print(v, end=' ')

	        for i in graph[v]:
		    if not visited[i]:
			queue.append(i)
			visited[i] = True
	```


#### Reference
[DFS & BFS](https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3)
