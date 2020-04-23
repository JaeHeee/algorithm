T = int(input())

def dfs(n):
    if check[n-1] == 1:
        return
    check[n-1] = 1
    if n not in graph.keys():
        return
    for a in graph[n]:
        dfs(a)

for i in range(T):
    graph = {}
    check = []
    result = 0
    V, E = map(int, input().split())
    check = [0]*V
    for j in range(E):
        k, value = map(int, input().split())
        if k in graph.keys():
            graph[k].append(value)
        else:
            graph[k] = [value]
    S, G = map(int, input().split())

    dfs(S)

    if check[G-1] == 1:
        result = 1

    print("#%d %d" % (i+1, result))
