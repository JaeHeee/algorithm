from queue import PriorityQueue


def solution(food_times, k):
    food_queue = PriorityQueue()

    if sum(food_times) <= k:
        return -1

    # 시간기준으로 food_time 우선순위큐로 만들기
    for i in range(len(food_times)):
        food_queue.put((food_times[i], i + 1))

    time_consuming = 0
    prev = 0
    length = len(food_times)

    while ((food_queue.queue[0][0] - prev) * length) <= k - time_consuming:
        now = food_queue.get()[0]  # time이 가장 작은 것
        time_consuming += (now - prev) * length  # while문 탈출하기 위해 저장
        length -= 1
        prev = now

    # 원래 순서대로 정렬 후 남는 것 찾기
    result = sorted(food_queue.queue, key=lambda x: x[1])
    k -= time_consuming

    return result[k % len(food_queue.queue)][1]