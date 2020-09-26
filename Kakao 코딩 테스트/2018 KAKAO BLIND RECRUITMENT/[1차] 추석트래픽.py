def solution(lines):
    answer = []
    times = []

    for line in lines:
        trans = float(line.split()[2][:-1])  # 처리시간
        time = line.split()[1]
        h, m, s = time.split(":")
        end = int(h) * 3600 + int(m) * 60 + float(s)  # 완료시간
        start = end - trans + 0.001  # 시작시간

        times.append((start, end))

    for t in times:
        print(t)

    for i in range(len(times)):
        count = 1
        for j in range(i + 1, len(times)):
            if times[j][0] - times[i][1] < 1:  # 1초이내인가 확인
                count += 1

        answer.append(count)

    return max(answer)
