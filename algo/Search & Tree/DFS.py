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

def dfs(node):
    if checked[node-1]:
        return
    checked[node-1] = True
    print(node, end=" ")
    for i in numbers[node]:
        dfs(i)

dfs(1)