# BAEKJOON 단지번호붙이기

def dfs(x, y):
    global number
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        number += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

result = 0
numbers = []
number = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            numbers.append(number)
            result += 1
            number = 0

print(result)
for num in sorted(numbers):
    print(num)
