def solution(m, n, puddles):
    answer = 0

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # 잠긴구역인지 확인
            if [j + 1, i + 1] in puddles:
                dp[i][j] = 0
            # 집인 경우
            elif i == 0 and j == 0:
                dp[i][j] = 1
            # 이 지점에 도달할 수 있는 방법의 수 계산
            else:
                if i == 0:
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    answer = dp[-1][-1]

    return answer % 1000000007