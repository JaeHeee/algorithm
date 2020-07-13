d = [0] * 100001
d[1] = 1
d[2] = 1


def fib(x):
    if x == 1:
        return 1
    if x == 2:
        return 1

    for i in range(3, x + 1):
        d[i] = d[i - 2] + d[i - 1]

    return d[x]


def solution(n):
    answer = fib(n)
    return answer % 1234567