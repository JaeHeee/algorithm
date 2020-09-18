import heapq


def solution(n, works):
    answer = 0
    # 모든 값에 -1을 곱해줍니다. 제일 큰 값을 제일 작은 값으로 만듭니다.
    works = [work * -1 for work in works]
    heapq.heapify(works)

    for i in range(n):
        num = heapq.heappop(works)
        if num == 0:
            break
        # 원래 제일 큰값을 +1는 해줍니다.
        heapq.heappush(works, num + 1)

    for work in works:
        answer += work ** 2

    return answer
