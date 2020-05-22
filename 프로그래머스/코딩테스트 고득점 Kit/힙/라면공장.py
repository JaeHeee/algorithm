import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    idx = 0
    while k > stock:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, (-supplies[i], supplies[i]))
                idx += 1
            else:
                break
        stock += heapq.heappop(heap)[1]
        answer += 1

    return answer