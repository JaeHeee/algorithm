## Sorting

- 정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말한다.
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용된다.


### 선택 정렬

- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다.
	
	``` python
	array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

	for i in range(len(array)):
		min_index = i
		for j in range(i+1, len(array)):
			if array[min_index] > array[j]:
				min_index = j
		array[i], array[min_index] = array[min_index], array[i]
	```

- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같다.

        N + (N-1) + (N-2) + ... + 2

- 이는 (N^2+N-2)/2 로 표현할 수 있는데, 빅오 표기법에 따라서 O(N^2)이라고 작성한다.


### 삽입 정렬

- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작한다.

	``` python
	array = [7, 5, 9 ,0, 3, 1, 6, 2, 4, 8]

	for i in range(1, len(array)):
		for j in range(i, 0, -1):
			if array[j] < array[j-1]:
				array[j], array[j-1] = array[j-1], array[j]
			else:
				break
	```

- 삽입 정렬의 시간 복잡도는 O(N^2)이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용된다.
- 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
	- 최선의 경우 O(N)의 시간 복잡도를 가진다.


### 퀵 정렬

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정
- 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)을 기대할 수 있다.
- 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다.
- 하지만 최악의 경우 O(N^2)의 시간 복잡도를 가진다.
	- 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행하는 경우

	``` python
	array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

	def quick_sort(array, start, end):
		if start >= end:
			return
		pivot = start
		left = start  1
		right = end
		while(left <= right):
			while(left <= end and array[left] <= array[pivot]):
				left += 1
			while(left > start and array[right] >= array[pivot]):
				left -= 1
			if(left > right):
				array[right], array[pivot] = array[pivot], array[right]
			else:
				array[left], array[right] = array[right], array[left]

		quick_sort(array, start, right - 1)
		quick_sort(array, right + 1, end)
	```
	- ver 2.0
	``` python
	array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

	def quick_sort(array):
		if len(array) <= 1:
			return array
		pivot = array[0]
		tail = array[1:]

		left_side = [x for x in tail if x <= pivot]
		right_side = [x for x in tail if x > pivot]

		return quick_sort(left_side) + [pivot] + quick_sort(right_side)
	```


### 계수 정렬

- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
	- 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K)를 보장
- 시간 복잡도와 공간 복잡도 모두 O(N+K)
- 때에 따라서 심각한 비효율성을 초래
	- 데이터가 0 과 999,999로 단 2개만 존재하는 경우
- 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적
	- 성적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적


	``` python
	array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

	count = [0] * (max(array) + 1)

	for i in range(len(array)):
		count[array[i]] += 1
	
	for i in range(len(count)):
		for j in range(count[i]):
			print(i, end=' ')
	```


### 정렬 알고리즘 비교

- 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장하도록 설계되어 있다.

|정렬 알고리즘|평균 시간 복잡도|공간 복잡도|특징|
|:---:|:---:|:---:|---|
|선택 정렬|O(N^2)|O(N)|아이디어가 매우 간단|
|삽입 정렬|O(N^2)|O(N)|데이터가 거의 정렬되어 있을 때는 가장 빠르다.|
|퀵 정렬|O(NlogN)|O(N)|대부분의 경우에 가장 적합, 충분히 빠르다.|
|계수 정렬|O(N+K)|O(N+K)|데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작한다.|

	  
#### Reference
[Sorting](https://www.youtube.com/watch?v=KGyK-pNvWos&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)
