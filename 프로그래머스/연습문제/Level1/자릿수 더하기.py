def solution(n):
    answer = 0
    n_length = len(str(n))

    for i in range(n_length):
        answer += n % 10
        n = n // 10

    return answer