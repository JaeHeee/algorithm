def solution(n):
    answer = 0
    numbers = []

    for i in range(n):
        numbers.append(i + 1)

    for i in range(1, n):
        if numbers[i] != 0:
            for j in range((i + 1) + (i + 1), n + 1, i + 1):
                numbers[j - 1] = 0
    answer = len(numbers) - 1 - numbers.count(0)
    return answer