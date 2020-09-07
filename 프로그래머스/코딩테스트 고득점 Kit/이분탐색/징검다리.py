def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    # dist = [rocks[0]]

    #     for i in range(1,len(rocks)):
    #         dist.append(rocks[i]-rocks[i-1])

    min_ = 0
    max_ = distance

    while min_ <= max_:
        mid = (max_ + min_) // 2
        prev = 0
        count = 0
        min_dist = 1e9
        # temp = dist[:]

        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                count += 1
            else:
                min_dist = min(min_dist, rocks[i] - prev)
                prev = rocks[i]

        #         for j in range(len(temp)):
        #             if temp[j] < mid:
        #                 count +=1
        #                 print(temp[j],mid)
        #             else:
        #                 min_dist = min(min_dist, temp[j])

        #         print(temp, min_dist, count)

        if count > n:
            max_ = mid - 1
        else:
            min_ = mid + 1
            answer = min_dist

    return answer