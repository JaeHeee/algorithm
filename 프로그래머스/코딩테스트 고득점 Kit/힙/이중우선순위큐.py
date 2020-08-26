import heapq

def solution(operations):
    answer = [0,0]
    heap = []

    for op in operations:
        op, num = op.split(" ")
        # heap 구조를 만듭니다.
        if op == 'I':
            heapq.heappush(heap,int(num))
        elif op =='D' and heap:
            # D 다음의 숫자가 양수이면 max_heap구조로 변환하고, max 삭제
            if int(num)>0:
                heapq._heapify_max(heap)
                heapq.heappop(heap)
                if heap:
                    heapq.heapify(heap)
            # 음수이면 min 삭제
            else:
                heapq.heappop(heap)
    
    if heap:
        return [max(heap), min(heap)]
    else:
        return answer