def solution(n, money):
    dp = [0] * (n + 1)

    for m in money:
        for i in range(1, n + 1):
            # 거스름돈이 m 이상이여야 거슬러줄 수 있음
            if i < m:
                continue
            if i == m:
                dp[i] += 1
            dp[i] += dp[i - m] % 1000000007

    return dp[-1]