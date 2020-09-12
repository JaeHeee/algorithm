def solution(n, lost, reserve):
    answer = n - len(lost)

    # 여벌 체육복을 가져왔고, 도난당한 학생
    dup = lost[:]
    for d in dup:
        if d in reserve:
            reserve.remove(d)
            lost.remove(d)
            answer += 1

    # 양쪽방향으로 여벌을 가지고 있는지 확인
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            answer += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            answer += 1

    return answer