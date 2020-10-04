def solution(n, t, m, timetable):
    answer = ''
    arrival = 540 + t * (n - 1)
    wait = []
    shuttle = []

    # 시간 분으로 계산
    for time in timetable:
        hour, minute = time.split(":")
        wait.append(int(hour) * 60 + int(minute))

    wait.sort()

    # shuttle 버스 탑승
    for i in range(n):
        shuttle.append([])
        count = 0
        while wait:
            if m == count or wait[0] > 540 + t * i:
                break
            if 540 + t * i >= wait[0] and count < m:
                shuttle[i].append(wait.pop(0))
                count += 1

    # 도착시간 계산
    if len(shuttle[-1]) == m:
        arrival = shuttle[-1][-1] - 1

    hour = arrival // 60
    minute = arrival % 60

    if hour < 10:
        answer += ("0" + str(hour) + ":")
    else:
        answer += (str(hour) + ":")

    if minute < 10:
        answer += ("0" + str(minute))
    else:
        answer += str(minute)

    return answer