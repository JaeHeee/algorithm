def solution(n):
    numbers = list(str(n))
    answer = [int(num) for num in reversed(numbers)]
    return answer