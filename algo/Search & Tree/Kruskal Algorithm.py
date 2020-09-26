# 가장적은 비용으로 모든 노드를 연결하는 알고리즘
# 비용을 기준으로 먼저 오름차순으로 정렬
# 정렬된 순서에 맞게 그래프에 포함
# 포함시키 전에 사이클 테이블 확인 (union find 이용)
# 사이클을 형성하는 경우 간선을 포함하지 않음

def getParent(parent, num):
    if parent[num] == num:
        return num
    else:
        return getParent(parent, parent[num])


def unionParent(parent, num1, num2):
    a = getParent(parent, num1)
    b = getParent(parent, num2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def findParent(parent, num1, num2):
    a = getParent(parent, num1)
    b = getParent(parent, num2)

    if a == b:
        return True
    elif a != b:
        return False

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

# 간선의 비용 오름차순으로 정렬
mygraph['edges'].sort()

# 각 정점이 포함된 그래프가 어디인지 저장
parents = dict()
for vertice in mygraph['vertices']:
    parents[vertice]=vertice

for edge in mygraph['edges']:
    if not findParent(parents, edge[1], edge[2]):
        unionParent(parents, edge[1], edge[2])
        print(edge)
