def solution(a, b):
    answer = ''
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    count = 0
    for m in range(a - 1):
        count += days[m]
    count += b
    answer = day[count % 7 - 1]

    return answer