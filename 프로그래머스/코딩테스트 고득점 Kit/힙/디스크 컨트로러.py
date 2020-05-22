import heapq as hq

def solution(jobs):
    answer = 0
    heap = []
    time = 0
    end = -1
    count = 0
    while count < len(jobs):
        for j in jobs:
            if end < j[0] <= time:
                hq.heappush(heap, j[1])
                answer += (time - j[0])
        if heap:
            answer += heap[0] * len(heap)
            end = time
            time += hq.heappop(heap)
            count += 1
        else:
            time += 1

    return answer // len(jobs)