T = int(input())

for i in range(T):
    N = int(input())

    result = []
    numbers = list(map(int, input().split()))

    while(numbers != []):
        if len(numbers) == 1:
            result.append(numbers[0])
            numbers.remove(numbers[0])
            break
        result.append(max(numbers))
        numbers.remove(max(numbers))
        result.append(min(numbers))
        numbers.remove(min(numbers))

    print("#%d" % (i + 1), end=' ')

    for r in range(10):
        print(str(result[r]), end=" ")
    print()
