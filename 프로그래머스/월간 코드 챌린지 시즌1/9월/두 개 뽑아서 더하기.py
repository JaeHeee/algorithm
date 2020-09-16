from itertools import combinations


def solution(numbers):
    answer = set()
    # 두 수의 조합
    comb = combinations(numbers, 2)

    for c in comb:
        answer.add(sum(c))

    return sorted(answer)