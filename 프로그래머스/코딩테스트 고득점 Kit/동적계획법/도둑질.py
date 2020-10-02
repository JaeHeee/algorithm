def solution(money):
    # 첫번째 집을 무조건 고려하는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    # 마지막 집을 무조건 고려하는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2))