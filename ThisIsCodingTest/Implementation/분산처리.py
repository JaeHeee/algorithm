# BAEKJOON 분산처리

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    '''
    1 -> 1
    2 -> 2, 4, 8, 6
    3 -> 3, 9, 7, 1
    4 -> 4, 6
    5 -> 5
    6 -> 6
    7 -> 7, 9, 3, 1
    8 -> 8, 4, 2, 6
    9 -> 9, 1
    10 -> 10
    ...
    '''
    if a in [1, 5, 6, 10]:
        print(a)
        continue
    
    numbers = []
    num = 1
    for _ in range(b):
        num *= a
        num %= 10
        if num in numbers:
            break
        numbers.append(num)
    
    answer = numbers[b%len(numbers) - 1]
    if answer:
        print(answer)
    else:
        print(10)
