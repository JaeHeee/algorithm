def solution(numbers, target):
    node = [0]
    for n in numbers:
        child = []
        for i in node:
            child.append(i + n)
            child.append(i - n)
        node = child

    return node.count(target)
