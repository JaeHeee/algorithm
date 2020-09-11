def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        binary = format(i | j, 'b') # i,j 각각의 2진수의 OR 연산
        binary = '0' * (n - len(binary)) + binary # binary의 길이가 지도 길이 보다 짧은 경우 0으로 채워줍니다.
        result = ''
        # 1인 부분 #으로 0 인 부분 공백으로
        for b in binary:
            if b == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)
    return answer
