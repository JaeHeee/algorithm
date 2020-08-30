from collections import defaultdict

def dfs(start, result_graph, checked):
    lose = set()

    if checked[start - 1]:
        return {start}

    checked[start - 1] = True
    for i in result_graph[start]:
        lose.add(i)
        l = dfs(i, result_graph, checked)
        lose = lose | l

    return lose


def solution(n, results):
    answer = 0
    wins = [0] * n
    loses = [0] * n

    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)

    for r in results:
        win_graph[r[0]].append(r[1])
        lose_graph[r[1]].append(r[0])

    for i in range(1, n + 1):
        checked_win = [0] * n
        checked_lose = [0] * n
        # dfs를 이용해서 이긴 선수와 진 선수들을 찾아냅니다.
        win = dfs(i, win_graph, checked_win)
        lose = dfs(i, lose_graph, checked_lose)
        wins[i - 1] = list(win)
        loses[i - 1] = list(lose)

    # 이긴 경기와 진 경기 수의 합이 n-1이면 answer에 추가
    for w, l in zip(wins, loses):
        if len(w) + len(l) == n - 1:
            answer += 1

    return answer