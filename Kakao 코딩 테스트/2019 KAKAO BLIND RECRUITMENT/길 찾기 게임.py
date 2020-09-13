import sys
sys.setrecursionlimit(10 ** 6)


# tree의 node
class Node:
    def __init__(self, x, id, left_bound, right_bound):
        self.x = x
        self.id = id
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.left_node = None
        self.right_node = None


preorder_result = []
postorder_result = []


#preorder
def preorder(node):
    preorder_result.append(node.id)

    if node.left_node:
        preorder(node.left_node)
    if node.right_node:
        preorder(node.right_node)


# postorder
def postorder(node):
    if node.left_node:
        postorder(node.left_node)
    if node.right_node:
        postorder(node.right_node)

    postorder_result.append(node.id)


def solution(nodeinfo):
    answer = [[]]
    # node 번호 추가
    nodeinfo = [node + [idx + 1] for idx, node in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: x[1], reverse=True)

    # level별로 node 모아주기
    levels = []
    level = -1
    for node in nodeinfo:
        if level != node[1]:
            levels.append([])
            level = node[1]
        levels[len(levels) - 1].append((node[0], node[2]))

    for level in levels:
        level.sort()

    root = Node(levels[0][0][0], levels[0][0][1], 0, 100000)

    # tree 만들기
    tree = [[]]
    tree[0].append(root)
    for level in levels[1:]:
        tree.append([])
        for data in level:
            x = data[0]
            id = data[1]
            for parent in tree[-2]:
                # 왼쪽 자식인 경우
                if parent.left_bound <= x and parent.x > x:
                    left_child = Node(x, id, parent.left_bound, parent.x)
                    parent.left_node = left_child
                    tree[-1].append(left_child)
                    break
                # 오른쪽 자식인 경우
                elif parent.right_bound >= x and parent.x < x:
                    right_child = Node(x, id, parent.x, parent.right_bound)
                    parent.right_node = right_child
                    tree[-1].append(right_child)
                    break

    preorder(root)
    postorder(root)

    return [preorder_result, postorder_result]

    return answer