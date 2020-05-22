import heapq


def solution(scoville, K):
    answer = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)
    while heap[0] < K and len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first + second * 2)
        answer += 1

    if len(heap) == 1 and heap[0] < K:
        answer = -1

    return answer