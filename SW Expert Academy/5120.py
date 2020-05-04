T = int(input())

for i in range(T):
    N, M, K = map(int, input().split())
    result = list(map(int, input().split()))
    idx = 0

    for j in range(K):
        length = len(result)
        if idx + M > length:
            temp = M - (length-idx)
            idx = 0
            if temp > length:
                temp //=length
            else:
                idx = temp
            result.insert(idx, result[idx - 1] + result[idx])
        elif idx + M == length:
            idx = -1
            result.append(result[-1] + result[0])
        else:
            idx += M
            result.insert(idx, result[idx - 1] + result[idx])

    print("#%d " % (i+1), end="")
    if len(result) > 10:
        print(' '.join(str(n) for n in result[-1:-11:-1]))
    else:
        print(' '.join(str(n) for n in result[-1:-len(result)-1:-1]))
