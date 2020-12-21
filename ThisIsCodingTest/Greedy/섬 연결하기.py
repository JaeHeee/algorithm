# 프로그래머스 섬 연결하기 문

def solution(n, costs):
    answer = 0
    island = set()
    count = 1 # 연결되 섬의 수

    costs.sort(key=lambda x: x[2])
    island.add(costs[0][0])

    while len(island) != n:
        for c in costs:
            if c[0] in island or c[1] in island:
                island.add(c[0])
                island.add(c[1])
                if len(island) > count:
                    count = len(island)
                    answer += c[2]
                    break
    
    return answer
