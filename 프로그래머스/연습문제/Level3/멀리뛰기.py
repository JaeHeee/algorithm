def solution(n):
    dp = [0] * (n + 1)
    # i까지 갈 수 있는 방법의 수 저장
    for i in range(0, n + 1):
        if i == 0 or i == 1:
            dp[i] += 1
        else:
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1] % 1234567