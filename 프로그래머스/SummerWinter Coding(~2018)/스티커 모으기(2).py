def solution(sticker):
    dp1 = [0] * 100001
    dp2 = [0] * 100001

    n = len(sticker)
    if n == 1:
        return sticker[0]

    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2[0] = 0
    dp2[1] = sticker[1]
    for j in range(2, n):
        dp2[j] = max(dp2[j - 1], dp2[j - 2] + sticker[j])

    answer = max(dp1[n - 2], dp2[n - 1])

    return answer