checked = [0] * 7
numbers = {
    1: [2,3],
    2: [1,3,4,5],
    3: [1,2,6,7],
    4: [2,5],
    5: [2,4],
    6: [3,7],
    7: [3,6]
}

def bfs(start):
    queue = []
    queue.append(start)
    checked[start-1] = True
    while queue:
        num = queue.pop(0)
        print(num, end=" ")
        for i in numbers[num]:
            if checked[i-1] == 0:
                queue.append(i)
                checked[i-1] = True

bfs(1)

