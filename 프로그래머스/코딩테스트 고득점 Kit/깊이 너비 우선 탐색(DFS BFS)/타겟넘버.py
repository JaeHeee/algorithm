def solution(numbers, target):
    node = [0]
    # 숫자를 하나씩 가져와서 +,- 하는 경우를 계산해서 추가합니다.
    for n in numbers:
        child = []
        for i in node:
            child.append(i + n)
            child.append(i - n)
        node = child

    return node.count(target)