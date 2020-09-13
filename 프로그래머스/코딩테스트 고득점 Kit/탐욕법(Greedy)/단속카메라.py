def solution(routes):
    answer = 0
    # 차량이 고속도로에서 나가는 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])

    while routes:
        route = routes.pop(0)

        for r in routes[:]:
            # 중복되는 지점 찾기
            if r[0] <= route[1] <= r[1]:
                routes.remove(r)

        answer += 1

    return answer