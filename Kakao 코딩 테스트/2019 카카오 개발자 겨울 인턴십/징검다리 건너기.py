def solution(stones, k):
    answer = 0
    _min = 0
    _max = 2e8

    while _min <= _max:
        mid = (_min + _max) // 2
        zero_count = 0
        for s in stones:
            if s >= mid:
                zero_count = 0
            elif s < mid:
                zero_count += 1
                if zero_count >= k:
                    break

        if zero_count >= k:
            _max = mid - 1
        else:
            answer = mid
            _min = mid + 1

    return answer
