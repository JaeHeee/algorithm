# 여러 개의 노드가 존재할 때 두 개의 노드를 선택해서, 현재 이 노드가 서로 같은 그래프에 속하는지 판별
# union : 부모를 합침. 일반적으로 더 작은 값 쪽으로 합침
# find : 두 개의 노드의 부모 노드를 확인하여 현재 같은 집합에 속하는지 확인

def getParent(parent, num):
    if parent[num] == num:
        return num
    else:
        return getParent(parent, parent[num])

# 부모 노드 합치기
def unionParent(parent, num1, num2):
    a = getParent(parent, num1)
    b = getParent(parent, num2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 같은 부모를 가지는가
def findParent(parent, num1, num2):
    a = getParent(parent, num1)
    b = getParent(parent, num2)

    if a == b:
        return 1
    elif a != b:
        return 0


parent = [0]

for i in range(1, 11):
    parent.append(i)
print(parent)

unionParent(parent, 1, 2)
unionParent(parent, 2, 3)
unionParent(parent, 3, 4)
unionParent(parent, 5, 6)
unionParent(parent, 6, 7)
unionParent(parent, 7, 8)
unionParent(parent, 1, 2)
print('1과 5는 연결되어 있나요? %d' % findParent(parent, 1, 5))
unionParent(parent, 1, 5)
print('1과 5는 연결되어 있나요? %d' % findParent(parent, 1, 5))

print(parent)
