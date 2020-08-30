def solution(N, stages):
    answer = []
    stage_count = []
    fail = []
    # stage별 카운트
    for n in range(1, N + 2):
        stage_count.append(stages.count(n))


    for n in range(N):
        # 아무도 스테이지에 도달하지 못하면 실패율 0
        if sum(stage_count[n:]) == 0:
            fail.append((n + 1, 0))
        # 실패율 계산
        else:
            fail.append((n + 1, stage_count[n] / sum(stage_count[n:])))
    fail.sort(key=lambda x: -x[1])

    for f in fail:
        answer.append(f[0])

    return answer