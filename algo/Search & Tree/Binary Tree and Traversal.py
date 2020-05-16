class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

nodes = []
for i in range(15):
    nodes.append(Node(i+1))

for i in range(14):
    if i % 2:
        nodes[i//2].left = nodes[i]
    else:
        nodes[i//2].right = nodes[i+2]


preorder(nodes[0])
print()
inorder(nodes[0])
print()
postorder(nodes[0])