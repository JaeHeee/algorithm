T = int(input())

for i in range(T):
    N, M, L = map(int, input().split())
    result = list(map(int, input().split()))

    for j in range(M):
        actions = list(map(str, input().split()))
        if actions[0] == 'I':
            result.insert(int(actions[1]), int(actions[2]))
        elif actions[0] == 'D':
            result.pop(int(actions[1]))
        else:
            result[int(actions[1])] = int(actions[2])

    if len(result) > L:
        print("#%d %d" % (i+1, result[L]))
    else:
        print("#%d %d" % (i + 1, -1))
