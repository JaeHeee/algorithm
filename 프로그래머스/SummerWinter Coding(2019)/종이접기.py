def inorder(idx, numbers, answer):
    if idx < len(numbers):
        inorder(2 * idx + 1, numbers, answer)
        answer.append(numbers[idx])
        inorder(2 * idx + 2, numbers, answer)


def solution(n):
    answer = []
    numbers = []
    for i in range(2 ** n - 1):
        if i == 0:
            numbers.append(0)
        elif i % 2:
            numbers.append(0)
        else:
            numbers.append(1)

    inorder(0, numbers, answer)

    return answer