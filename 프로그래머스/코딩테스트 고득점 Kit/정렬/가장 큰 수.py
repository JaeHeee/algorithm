def solution(numbers):
    answer = ''
    # 각 숫자들을 문자로 만들어서 리스트에 저장
    str_num = [str(n) for n in numbers]
    # 모든 숫자는 1000이하이므로 3을 곱한 것을 기준으로 정렬
    str_num.sort(key=lambda x: x * 3, reverse=True)

    for s in str_num:
        answer += s

    # 맨 앞이 0인 경우
    if answer[0] == '0':
        answer = str(int(answer))

    return answer