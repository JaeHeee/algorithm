def binary_search(low, high, times, n):
    if low > high:
        return high + 1
    mid = (low + high) // 2
    people = 0

    # 몇명까지 심사할 수 있는지 계산
    for t in times:
        people += mid // t

    if n == people:
        # 최솟값을 찾아야 하므로 1초 단축한 시간도 확인
        return min(mid, binary_search(low, mid - 1, times, n))
    elif n < people:
        return binary_search(low, mid - 1, times, n)
    else:
        return binary_search(mid + 1, high, times, n)


def solution(n, times):
    answer = binary_search(0, n * max(times), times, n)

    return answer