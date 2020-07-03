def solution(n):
    answer = ''
    numbers = list(str(n))
    numbers.sort(reverse = True)
    for num in numbers:
        answer += num
    return int(answer)