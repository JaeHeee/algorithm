#tree traversal

N = int(input(''))
node = []
for i in range(N):
    node.append(list(input('').split()))

def left(node,name):
    for i in node:
        if i[0]==name:
            return i[1]

def right(node,name):
    for i in node:
        if i[0]==name:
            return i[2]

def root(node,name):
    for i in node:
        if i[1]==name or i[2]==name:
            return i[0]

def search(node,name):
    for i in node:
        if i[0]==name:
            return node.index(i)

def preorder(node,i):
    print(node[i][0], end='')
    if node[i][1] != '.': # left child 존재
        left_child = left(node,node[i][0])
        j = search(node,left_child)
        preorder(node,j)
    if node[i][2] != '.':#right child 존재
        right_child = right(node,node[i][0])
        k = search(node,right_child)
        preorder(node,k)

def inorder(node,i):
    if node[i][1] != '.': # left child 존재
        left_child = left(node,node[i][0])
        j = search(node,left_child)
        inorder(node,j)
    print(node[i][0], end='')
    if node[i][2] != '.':#right child 존재
        right_child = right(node,node[i][0])
        k = search(node,right_child)
        inorder(node,k)

def postorder(node,i):
    if node[i][1] != '.': # left child 존재
        left_child = left(node,node[i][0])
        j = search(node,left_child)
        postorder(node,j)
    if node[i][2] != '.':#right child 존재
        right_child = right(node,node[i][0])
        k = search(node,right_child)
        postorder(node,k)
    print(node[i][0], end='')

preorder(node,0)
print()
inorder(node,0)
print()
postorder(node,0)
