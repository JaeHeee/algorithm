# 이동경로
def move(N, start, to, answer):
    answer.append([start, to])

# 하노이탑 함수
def hanoi(N, start, to, via, answer):
    if N == 1:
        move(1, start, to, answer)
    else:
        hanoi(N - 1, start, via, to, answer)  # 나머지 원판을 중간지점으로
        move(N, start, to, answer)  # 제일 큰 원판을 마지막 기둥으로
        hanoi(N - 1, via, to, start, answer)  # 나머지 원판을 마지막 기둥으로


def solution(n):
    answer = []

    hanoi(n, 1, 3, 2, answer)

    return answer
