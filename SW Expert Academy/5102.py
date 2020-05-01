T = int(input())


def bfs(s, g):
    global result
    path.append(s)
    visited[s-1] = 1

    while path:
        current = path.pop(0)

        for n in graph[current]:
            if visited[n-1] == 0:
                path.append(n)
                visited[n-1] = 1
                distance[n-1] = distance[current-1] + 1

                if n == g:
                    result = distance[n-1]
                    return
    return


for i in range(T):
    V, E = map(int, input().split())

    graph = {(l+1): [] for l in range(V)}
    for j in range(E):
        k, value = map(int, input().split())
        graph[k].append(value)
        graph[value].append(k)

    S, G = map(int, input().split())

    result = 0
    path = []
    visited = [0]*V
    distance = [0]*V

    bfs(S, G)

    print("#%d %d" % (i+1, result))
