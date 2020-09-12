def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        # 숫자를 붙여주는 경우
        dp[i].add(int(str(N) * (i)))

        if number in dp[i]:
            answer = i
            break

        if i > 1:
            # 전 단계들의 조합으로 계산
            for j in range(1, i // 2 + 1):
                for k in dp[j]:
                    dp[i] |= set(map((lambda x: x * k), dp[i - j]))
                    dp[i] |= set(map((lambda x: x + k), dp[i - j]))
                    dp[i] |= set(map((lambda x: x - k), dp[i - j]))
                    dp[i] |= set(map((lambda x: k - x), dp[i - j]))
                    dp[i] |= set(map((lambda x: x // k if k != 0 else 0), dp[i - j]))
                    dp[i] |= set(map((lambda x: k // x if x != 0 else 0), dp[i - j]))

            if number in dp[i]:
                answer = i
                break

    if answer:
        return answer
    else:
        return -1