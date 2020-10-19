def solution(n):
    answer = 0
    numbers = []
    # 3진법 계산
    while n >= 3:
        numbers.append(n % 3)
        n //= 3
    numbers.append(n)

    # 10진법 계산
    for idx, num in enumerate(numbers[::-1]):
        answer += num * (3 ** idx)

    return answer