def bfs(start, maps, distance, K):
    distance[start] = 0
    checked = []
    checked.append(start)

    while checked:
        c = checked.pop(0)
        for m in range(1, len(maps)):
            if maps[c][m]:
                if distance[c] + maps[c][m] <= K and distance[m] > distance[c] + maps[c][m]:
                    distance[m] = distance[c] + maps[c][m]
                    checked.append(m)


def solution(N, road, K):
    answer = 1
    distance = [500001 for i in range(N + 1)]
    maps = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for frm, to, w in road:
        if maps[frm][to] == 0 and maps[to][frm] == 0:
            maps[frm][to], maps[to][frm] = w, w
        else:
            if w < maps[frm][to]:
                maps[frm][to], maps[to][frm] = w, w

    bfs(1, maps, distance, K)

    answer = len([d for d in distance if d <= K])

    return answer