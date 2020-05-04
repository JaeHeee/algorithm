T = int(input())


def search(t, idx):
    global count
    if t[idx-1]:
        count += 1
        for pos in t[idx-1]:
            search(t, pos)
    else:
        count += 1
        return


for i in range(T):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[] for j in range(E+1)]
    for n in range(0, 2*E, 2):
        tree[nodes[n]-1].append(nodes[n+1])

    count = 0

    search(tree, N)

    print("#%d %d" % (i+1, count))
