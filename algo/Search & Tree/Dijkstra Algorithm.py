# 다이나믹 프로그래밍을 활용한 최단경로 탐색 알고리즘
# 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단경로 찾기
# 최단 거리는 여러 개의 최단 거리로 이루어져 있다.
# 하나의 최단 거리를 구할 때 그 이전까지 구했던 최단 거리 정보를 그대로 사용
# 현재까지 알고 있던 최단 경로를 계속해서 갱신
# 1. 출발 노드 설정
# 2. 출발 노드를 기준으로 각 노드의 최소 비용 저장
# 3. 방문하지 않은 노드중에서 가장 비용이 적은 노드 선택
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용을 갱신
# 5. 3~4번 반복

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        # distance 계산
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            # distances 갱신
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


print(dijkstra(mygraph, 'A'))