def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    # 각 바위 사이의 거리
    dist = [rocks[0]]
    for i in range(1,len(rocks)):
        dist.append(rocks[i]-rocks[i-1])

    min_ = 0
    max_ = distance

    while min_ <= max_:
        mid = (max_ + min_) // 2
        count = 0
        min_dist = 1e9
        temp = dist[:]

        for j in range(len(temp)):
            if temp[j] < mid:
                count += 1
                # 마지막이 아닌 경우
                if j != len(temp)-1:
                    temp[j+1] += temp[j]
            else:
                min_dist = min(min_dist, temp[j])

        if count > n:
            max_ = mid - 1
        else:
            min_ = mid + 1
            answer = min_dist

    return answer
