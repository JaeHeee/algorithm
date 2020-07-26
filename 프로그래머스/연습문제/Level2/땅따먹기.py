def solution(land):
    answer = 0
    dp = []

    for i in range(100000):
        dp.append([])
        for j in range(4):
            dp[i].append(0)

    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i - 1][k])

    answer = max(dp[len(land) - 1])

    return answer