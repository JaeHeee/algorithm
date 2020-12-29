# Programmers 네트워크

def dfs(computers, visited, start):
    if visited[start]:
        return
    
    visited[start] = 1
    for idx, c in enumerate(computers[start]):
        if c == 1:
            dfs(computers, visited, idx)


def solution(n, computers):
    answer = 0
    visited = [0] * n

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1

    return answer
