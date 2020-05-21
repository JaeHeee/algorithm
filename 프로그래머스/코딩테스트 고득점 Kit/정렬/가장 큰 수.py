def solution(numbers):
    answer = ''
    str_num = [str(n) for n in numbers]
    str_num.sort(key=lambda x: x * 3, reverse=True)
    for s in str_num:
        answer += s
    if answer[0] == '0':
        answer = str(int(answer))

    return answer