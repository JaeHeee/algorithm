# BAEKJOON DFS & BFS

from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    dfs_list.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        bfs_list.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, start = map(int, input().split())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for node in graph:
    node.sort()

dfs_list = []
dfs(graph, start, visited[:])
print(*dfs_list)

bfs_list = []
bfs(graph, start, visited[:])
print(*bfs_list)
