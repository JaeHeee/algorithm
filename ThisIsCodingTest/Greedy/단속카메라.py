# 프로그래머스 단속카메라

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])

    while routes:
        route = routes.pop(0)

        for r in routes[:]:
            if r[0] <= route[1] <= r[1]:
                routes.remove(r)

        answer += 1

    return answer
