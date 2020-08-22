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

    if num < n:
        if n > 10 and 10 <= num <= 15:
            num = alpa[num]
        number.append(num)
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

    for num in range(t * m + 1):
        number = transform(n, num)
        numbers += number

    for j in range(t):
        answer += str(numbers[(p - 1) + j * m])

    return answer