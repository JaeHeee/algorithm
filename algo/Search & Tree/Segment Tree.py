# 여러 개의 데이터가 연속적으로 존재할 때 특정한 범위의 데이터의 합을 구하는 방법
# 구간 합 트리 생성
# 최상단 노드에는 전체 원소의 합이 들어감
# 원래의 데이터의 범위를 절반씩 분할하며 그 구간의 합들을 저장하도록 초기 설정을 함
# 데이터의 크기가 n개일때 n보다 큰 가장 가까운 n의 제곱수를 구한 뒤에
# 그것의 2배까지 미리 배열의 크기를 미리 만들어놓아야

numbers = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
tree = [0]*4*len(numbers)

def init_(start, end, node):
    if start == end:
        tree[node] = numbers[node]
        return tree[node]

    mid = start + end // 2
    tree[node] = init_(start, mid, node*2) + init_(mid+1, end, node*2)
    return tree[node]


# left, right : 구간 합을 구하고자 하는 범위
def sum_(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = start+end//2
    return sum_(start, mid, node*2, left, right) + sum_(mid+1, end, node*2+1, left, right)


def update(start, end, node, index, dif):
    if index < start or index > end:
        return
    tree[node] += dif
    if start == end:
        return
    mid = start+end//2
    update(start, mid, node*2, index, dif)
    update(mid+1, end, node*2+1, index, dif)

