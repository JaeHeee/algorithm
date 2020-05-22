def count(word, target):
    num = 0
    for idx, w in enumerate(word):
        if w != target[idx]:
            num += 1
    return num


def bfs(begin, target, words, visited, answer):
    queue = []
    queue.append(begin)
    while queue:
        word = queue.pop()

        if word == target:
            print(answer)
            return answer

        for i in range(0, len(words)):
            if count(words[i], word) == 1:
                if visited[i] == 1:
                    continue
                visited[i] = 1
                queue.append(words[i])
        answer += 1

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    visited = [0] * len(words)

    answer = bfs(begin, target, words, visited, answer)

    return answer