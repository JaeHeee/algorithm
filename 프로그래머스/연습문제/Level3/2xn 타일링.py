def solution(n):
    dp = [0] * (n + 1)
    answer = 0

    for i in range(1, n + 1):
        if i == 1 or i == 2:
            dp[i] += i
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    answer = dp[-1]

    return answer