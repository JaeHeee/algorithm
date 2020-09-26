def nqueen(sol, n):
    global answer
    if len(sol) == n:
        answer += 1
        return

    candidate = list(range(n))  # 0 부터 N-1 까지로 구성된 후보
    for i in range(len(sol)):
        if sol[i] in candidate:  # 같은 열에 놓이는지 확인
            candidate.remove(sol[i])

        distance = len(sol) - i  # 같은 대각선에 놓이는지 확인
        if sol[i] + distance in candidate:
            candidate.remove(sol[i] + distance)
        if sol[i] - distance in candidate:
            candidate.remove(sol[i] - distance)

    if candidate:  # 다음칸 진행
        for c in candidate:
            sol.append(c)
            nqueen(sol, n)
            sol.pop()
    else:
        return 0


def solution(n):
    global answer
    answer = 0

    for i in range(n):
        nqueen([i], n)

    return answer

