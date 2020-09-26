# 모든 정점에서 모든 정점으로의 최단경로 구하기
# 거쳐가는 정점을 기준으로 최단거리 계산
# 바로가는 비용과 거쳐서 가는 비용 비교

graph = [[0, 5, float('inf'), 8],
         [7, 0, 9, float('inf')],
         [2, float('inf'), 0, 4],
         [float('inf'), float('inf'), 3, 0]]


def floydWarshall():
    dp = [[0]*len(graph) for _ in range(len(graph))]

    for i in range(len(graph)):
        for j in range(len(graph)):
            dp[i][j] = graph[i][j]

    # via = 거쳐가는 노드
    for via in range(len(graph)):
        for start in range(len(graph)):
            for end in range(len(graph)):
                if dp[start][via] + dp[via][end] < dp[start][end]:
                    dp[start][end] = dp[start][via] + dp[via][end]

    for i in range(len(graph)):
        for j in range(len(graph)):
            print(dp[i][j], end=" ")
        print()

floydWarshall()