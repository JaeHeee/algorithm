from itertools import permutations


def check(base, answer, strike, ball):
    strike_count = 0
    for i in range(3):
        if base[i] == answer[i]:
            strike_count += 1
    if strike != strike_count:
        return False
    ball_count = len(set(base) & set(answer)) - strike
    if ball_count != ball:
        return False
    return True


def solution(baseball):
    answer = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for b in baseball:
        for a in answer[:]:
            if not check([int(n) for n in str(b[0])], a, b[1], b[2]):
                answer.remove(a)

    return len(answer)
