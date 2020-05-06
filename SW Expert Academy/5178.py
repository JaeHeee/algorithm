T = int(input())

def postorder(pos):
    if pos >= N:
        return 0
    if tree[pos] == 0:
        lc = postorder(pos*2+1)
        rc = postorder(pos*2+2)
        tree[pos] = lc + rc
    return tree[pos]

for i in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * N

    for j in range(M):
        idx, num = map(int, input().split())
        tree[idx - 1] = num

    postorder(0)

    print("#%d %d" % (i+1, tree[L-1]))
