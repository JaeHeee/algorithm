def solution(s):
    answer = ''
    splitted_s = s.split(' ')

    for string in splitted_s:
        for idx, value in enumerate(string):
            if idx % 2 == 0:
                answer += value.upper()
            else:
                answer += value.lower()
        answer += ' '
    answer = answer[:-1]
    return answer