def transform(n, num):
    number = []
    alpa = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    # n진법 보다 해당 숫자가 작을경우
    if num < n:
        if n > 10 and 10 <= num <= 15:
            num = alpa[num]
        number.append(num)
    # n진법 보다 해당 숫자가 클경우 n진법 계산
    else:
        temp = transform(n, num // n)
        number += temp
        mod = num % n
        if n > 10 and 10 <= mod <= 15:
            mod = alpa[mod]
        number.append(mod)

    return number


def solution(n, t, m, p):
    answer = ''
    numbers = []

    # 계산해야할 숫자의 최소갯수 = t*m
    for num in range(t * m + 1):
        number = transform(n, num)
        numbers += number

    # 순서에 해당하는 숫자만 추가
    for j in range(t):
        answer += str(numbers[(p - 1) + j * m])

    return answer