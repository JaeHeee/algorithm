def solution(n, k):
    answer = []
    numbers = [i + 1 for i in range(n)]

    # 전체 가능한 경우의 수 factorial
    fac = 1
    for i in range(1, n + 1):
        fac *= i

    while n > 0:
        # n-1! 단위의 블럭
        fac //= n
        idx = k // fac
        k = k % fac

        if k == 0:
            answer.append(numbers.pop(idx - 1))
        else:
            answer.append(numbers.pop(idx))

        n -= 1

    return answer