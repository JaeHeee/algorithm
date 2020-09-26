# 트리구조에서 특정한 두 노드의 공통된 조상 중에서 가장 가까운 조상
# 모든 노드에 대한 깊이 계싼
# 모든 노드에 대한 2^i 번째 부모 노드 계산
# 최소 공통 조상을 찾을 두 노드 설정
# 두 노드의 깊이가 동일하도록 거슬러 올라감
# 최상단 노드부터 내려오는 방식으로 두 노드의 공통 부모 찾아냄

depths = [0]*1001
check = [0]*1001
tree= []
parents = [[0]*11 for _ in range(1001)]


# 모든 깊이정보 저장
def dfs(x, depth):
    check[x] = True
    depths[x] = depth

    for i in range(len(tree[x])):
        data = tree[x][i]
        if check[data]:
            continue

        parents[data][0]=x
        dfs(data, depth+1)


# 부모 관계 설정
def setParent():
    dfs(0, 0) # root를 0으로 설정
    for j in range(1, 11):
        for i in range(21):
            parents[i][j] = parents[parents[i][j-1]][j-1]


# 최소 공통 조상 찾기
def LCA(x, y):
    if depths[x] > depths[y]:
        x, y = y, x
    # 노드의 깊이가 동일하도록
    for i in range(10, -1, -1):
        if depths[y]-depths[x] >= (1 << i):
            y = parents[y][i]

    # 부모가 같은 경우 반환
    if x==y:
        return x

    for i in range(10, -1, -1):
        if parents[x][i] != parents[y][i]:
            x = parents[x][i]
            y = parents[y][i]

    return parents[x][0]