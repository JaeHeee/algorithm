def solution(triangle):
    dp = []

    # 삼각형 아래에서부터 거꾸로 올라가면서 dp 계산
    for i, tri in enumerate(triangle[::-1]):
        if i == 0:
            dp.append(tri)
        else:
            dp.append([0] * len(tri))
            for j in range(len(tri)):
                dp[i][j] = max(tri[j] + dp[i - 1][j], tri[j] + dp[i - 1][j + 1])

    return dp[-1][0]
