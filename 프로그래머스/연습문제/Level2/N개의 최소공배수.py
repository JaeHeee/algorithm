def solution(arr):
    answer = 0
    max_ = max(arr)

    while True:
        count = 0
        for num in arr:
            if max_ % num != 0:
                count += 1

        if count == 0:
            return max_
        else:
            max_ += 1