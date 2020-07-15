def solution(s):
    answer = ''
    answer += s[0].upper()

    s = s.lower()

    check = False
    for i in s[1:]:
        if i == ' ':
            check = True
        elif check:
            answer += i.upper()
            check = False
            continue

        answer += i

    return answer