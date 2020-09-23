def solution(n, s):
    answer = []

    # 최고의 집합이 존재하지 않는 경우
    if n > s:
        return [-1]

    # 몫으로 채워주기
    answer = [s // n for _ in range(n)]

    # 뒤에서부터 1씩 증가시켜주기
    for i in range(1, s % n + 1):
        answer[-i] += 1

    return answer