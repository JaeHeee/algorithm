def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    add_ = 0

    for i in range(2, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + add_ * 2
        add_ += dp[i - 2]

    return dp[-1] % 1000000007