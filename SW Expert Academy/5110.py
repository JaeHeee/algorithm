T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    result = list(map(int, input().split()))

    for l in range(1, M):
        numbers = list(map(int, input().split()))
        for idx, n in enumerate(result):
            if numbers[0] < n:
                result[idx : idx] = numbers
                break
        if len(result) == N * l:
            result += numbers


    print("#%d " % (i+1), end="")
    print(' '.join(str(n) for n in result[-1:-11:-1]))
