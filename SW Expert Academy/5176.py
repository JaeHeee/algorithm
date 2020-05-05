T = int(input())

def inorder(n):
    global count
    if n <= N:
        inorder(2*n)
        tree[n] = count
        count += 1
        inorder(2*n +1)

for i in range(T):
    N = int(input())
    tree = [0] * (N+1);

    count = 1
    inorder(1)
    print("#%d %d %d" % (i+1, tree[1], tree[N//2]))
