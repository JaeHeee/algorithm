T = int(input())

for k in range(T):
    candidate = []
    N, M = map(int, input().split(" "))
    number = list(map(int, input().split(" ")))

    for i in range(0, N-M+1):
        sum = 0
        for j in range(i, i+M):
            sum += number[j]
        candidate.append(sum)

    print("#%d %d" % (k+1, max(candidate) - min(candidate)))

