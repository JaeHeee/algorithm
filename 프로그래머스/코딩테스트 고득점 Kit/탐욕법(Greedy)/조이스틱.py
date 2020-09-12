def solution(name):
    answer = 0
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    joy = ['A'] * len(name)
    alpha = []
    name = list(name)
    idx = 0

    # 이름에 A가 아닌 문자 있으면 alpha에 추가
    for j, n in zip(joy, name):
        if j != n:
            alpha.append(n)

    # 알파벳 커서 이동횟수 추가
    for a in alpha:
        answer += min(alphabets.index(a), 26 - alphabets.index(a))

    while True:
        # 좌우 한칸씩
        right = 1
        left = 1

        if name[idx] != 'A':
            name[idx] = 'A'

        if name == joy:
            break
        else:
            for i in range(1, len(name)):
                # 오른쪽 이나 왼쪽이 A 이면 이동할 칸 수 추가
                if name[idx + i] == 'A':
                    right += 1
                else:
                    break
                if name[idx - i] == 'A':
                    left += 1
                else:
                    break

            # 더 적은 칸수로 이동
            if right > left:
                answer += left
                idx -= left
            else:
                answer += right
                idx += right

    return answer