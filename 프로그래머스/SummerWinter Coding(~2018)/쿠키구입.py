def solution(cookie):
    answer = 0
    N = len(cookie) - 1
    for m in range(0, N):
        first_idx = m
        second_idx = m + 1
        first = cookie[first_idx]
        second = cookie[second_idx]

        while True:
            if first == second:
                answer = max(first, answer)
            if first_idx > 0 and first <= second:
                first_idx -= 1
                first += cookie[first_idx]
            elif second_idx < N and first >= second:
                second_idx += 1
                second += cookie[second_idx]
            else:
                break

    return answer