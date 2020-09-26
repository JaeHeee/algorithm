# 순서가 정해져있는 작업을 차례로 수행해야할 때 그 순서를 결정해주기 위해 사용
# 큐를 사용
# 1. 진입 차수가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내 연결된 모든 간선을 제거
# 3. 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입
# 4. 큐가 빌 때까지 2번 ~ 3번 과정을 반복합
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것이고,
# 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과

graph = [[],
         [2, 5],
         [3],
         [4],
         [6],
         [6],
         [7],
         []]
degree = [0, 0, 1, 1, 1, 1, 2, 1]

def topologySort():
    result = [0]*10
    queue = []

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,8):
        if degree[i] == 0:
            queue.append(i)

    # 정렬이 완전히 수행되려면 정확히 n개의 노드를 방문
    for i in range(1, 8):
        # 사이클 발생
        if queue == []:
            return

        x = queue.pop(0)
        result[i] = x
        for j in range(len(graph[x])):
            degree[graph[x][j]] -= 1
            # 새롭게 진입차수가 0이 된 정점을 큐에 삽입
            if degree[graph[x][j]] == 0:
                queue.append(graph[x][j])

    for k in range(1, 8):
        print(result[k], end=" ")

topologySort()