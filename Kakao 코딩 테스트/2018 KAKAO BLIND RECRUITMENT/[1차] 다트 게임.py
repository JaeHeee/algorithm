def solution(dartResult):
    area = ['S', 'D', 'T']
    prize_s = [0, 0, 0]  # 스타상
    prize_a = [0, 0, 0]  # 아차상
    answer = []
    cal = 0
    count = len(answer)
    for r in dartResult:
        # 숫자인 경우
        if r.isdigit():
            if cal != 0:
                # 숫자가 두자수 인 경우
                cal = int(str(cal) + r)
            else:
                cal = int(r)
                count += 1
        # 보너스
        elif r in area:
            cal = cal ** (area.index(r) + 1)
            answer.append(cal)
            cal = 0
        # 옵션
        elif r == '*':
            # 스타상이 첫번째에 나온 경우
            if count == 1:
                prize_s[0] += 1
            else:
                prize_s[count - 1] += 1
                prize_s[count - 2] += 1
        else:
            prize_a[count - 1] += 1

    result = 0
    for r, s, a in zip(answer, prize_s, prize_a):
        temp = r
        # 중첩을 고려해서 옵션을 적용
        if s != 0:
            temp *= (2 ** s)
        if a != 0:
            temp *= -1
        result += temp

    return result