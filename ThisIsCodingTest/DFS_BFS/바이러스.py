# BAEKJOON 바이러스

def dfs(graph, start, visited):
    visited[start] = 1

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)
    
    return visited.count(1) - 1


n = int(input())
pair = int(input())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(pair):
    com1, com2 = map(int, input().split())
    graph[com1].append(com2)
    graph[com2].append(com1)

print(dfs(graph, 1, visited))
