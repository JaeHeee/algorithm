def solution(dartResult):
    area = ['S', 'D', 'T']
    prize_s = [0, 0, 0]
    prize_a = [0, 0, 0]
    answer = []
    cal = 0
    count = len(answer)
    for r in dartResult:
        if r.isdigit():
            if cal != 0:
                cal = int(str(cal) + r)
            else:
                cal = int(r)
                count += 1
        elif r in area:
            cal = cal ** (area.index(r) + 1)
            answer.append(cal)
            cal = 0
        elif r == '*':
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
        if s != 0:
            temp *= (2 ** s)
        if a != 0:
            temp *= -1
        result += temp

    return result