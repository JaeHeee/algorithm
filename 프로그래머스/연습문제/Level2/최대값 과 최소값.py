def solution(s):
    answer = ' '
    numbers = list(map(int, s.split(' ')))

    max_ = max(numbers)
    min_ = min(numbers)

    answer = str(min_) + answer + str(max_)
    return answer