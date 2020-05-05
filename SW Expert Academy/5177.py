T = int(input())


for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    for n in range(1, N):
        idx = n
        while idx != 0:
            root = (idx-1)//2
            if numbers[root] > numbers[idx]:
                numbers[root], numbers[idx] = numbers[idx], numbers[root]
            idx = root

    total = 0
    check = N-1
    while check != 0:
        check = (check-1)//2
        total += numbers[check]

    print("#%d %d" % (i+1, total))
