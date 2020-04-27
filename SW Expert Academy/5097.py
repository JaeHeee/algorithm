T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    result = list(map(int, input().split()))

    for j in range(M):
        temp = result.pop(0)
        result.append(temp)

    print("#%d %d" % (i + 1, result[0]))
