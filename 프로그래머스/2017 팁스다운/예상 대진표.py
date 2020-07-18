def solution(n, a, b):
    answer = 1
    final = [1, 2]
    ab = [a, b]
    ab.sort()

    while ab != final:
        if ab[0] + 1 == ab[1] and ab[1] % 2 == 0:
            break

        answer += 1

        if ab[0] != 1:
            if ab[0] % 2 == 0:
                ab[0] //= 2
            else:
                ab[0] = ab[0] // 2 + 1

        if ab[1] != 2:
            if ab[1] % 2 == 0:
                ab[1] //= 2
            else:
                ab[1] = ab[1] // 2 + 1

    return answer