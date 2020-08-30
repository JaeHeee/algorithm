from collections import defaultdict

# bfs 이용해서 노드별 최단경로 저장
def bfs(start, graph):
    queue = []
    queue.append(start)
    checked = [0] * len(graph)
    path_length = [0] * len(graph) # 최단경로
    checked[0] = True

    while queue:
        node = queue.pop(0)
        for n in graph[node]:
            if checked[n - 1] == 0:
                queue.append(n)
                checked[n - 1] = True
                path_length[n - 1] = path_length[node - 1] + 1

    return path_length


def solution(n, edge):
    graph = defaultdict(list)

    # 그래프 만들
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    path_length = bfs(1, graph)

    if max(path_length):
        answer = path_length.count(max(path_length))
        return answer
    else:
        return 0