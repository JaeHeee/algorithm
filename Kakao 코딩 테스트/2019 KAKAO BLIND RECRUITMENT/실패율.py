def solution(N, stages):
    answer = []
    stage_count = []
    fail = []
    for n in range(1, N + 2):
        stage_count.append(stages.count(n))

    for n in range(N):
        if sum(stage_count[n:]) == 0:
            fail.append((n + 1, 0))
        else:
            fail.append((n + 1, stage_count[n] / sum(stage_count[n:])))
    fail.sort(key=lambda x: -x[1])

    for f in fail:
        answer.append(f[0])

    return answer