def solution(n, costs):
    answer = 0
    island = set()
    count = 1

    # cost가 작은 순서대로 정렬
    costs.sort(key=lambda x: x[2])
    island.add(costs[0][0])

    while len(island) != n:
        for c in costs:
            # 하나라도 있어야 연결가능
            if c[0] in island or c[1] in island:
                island.add(c[0])
                island.add(c[1])
                # len(island) == count 이면 이미 연결된 상황
                if len(island) > count:
                    count = len(island)
                    answer += c[2]
                    break

    return answer