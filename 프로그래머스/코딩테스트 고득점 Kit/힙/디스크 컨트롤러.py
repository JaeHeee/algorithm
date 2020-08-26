import heapq

def solution(jobs):
    answer = []
    time = 0
    disk_heap = []

    while jobs:
        for j in jobs:
            # 현재 시간 이전에 요청된 작업들을 작업시간을 기준으로 하여 힙 구조로 만들어줍니다.
            if j[0] <= time:
                heapq.heappush(disk_heap, (j[1], j))
        
        # 힙에서 가장 먼저 작업해야할 것을 빼고 시간을 더해줍니다.
        # answer에는 요청시간으로 부터 소요된 시간을 추가합니다.
        # 작업이 완료되면 jobs에서 제거합니다.
        if disk_heap:
            disk = heapq.heappop(disk_heap)
            time += disk[1][1]
            answer.append(time-disk[1][0])
            jobs.remove(disk[1])
            disk_heap=[]
        else:
            time+=1

    return sum(answer)//len(answer)