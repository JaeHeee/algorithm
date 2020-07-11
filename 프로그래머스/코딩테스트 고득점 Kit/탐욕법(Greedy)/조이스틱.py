def solution(name):
    answer = 0
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    joy = ['A'] * len(name)
    alpha = []
    name = list(name)
    idx = 0

    for j, n in zip(joy, name):
        if j != n:
            alpha.append(n)

    for a in alpha:
        answer += min(alphabets.index(a), 26 - alphabets.index(a))

    while True:
        right = 1
        left = 1

        if name[idx] != 'A':
            name[idx] = 'A'

        if name == joy:
            break
        else:
            for i in range(1, len(name)):
                if name[idx + i] == 'A':
                    right += 1
                else:
                    break
                if name[idx - i] == 'A':
                    left += 1
                else:
                    break

            if right > left:
                answer += left
                idx -= left
            else:
                answer += right
                idx += right

    return answer