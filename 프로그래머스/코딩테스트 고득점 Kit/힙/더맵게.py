import heapq

def solution(scoville, K):
    answer = 0
    # scoville 리스트를 heap구조로 만들어줍니다.
    heapq.heapify(scoville)

    # 모든 스코빌 지수가 K보다 큰 수가 되도록 만들어줍니다.
    while scoville[0] <K and len(scoville)>1:
        answer += 1
        mixed = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, mixed)

    # 모든 스코빌 지수를 K이상으로 만들 수 없는 경우
    if scoville[0] < K:
        answer = -1

    return answer