def solution(stones, k):
    answer = 0
    # 건널수 있는 친구들 최소, 최대
    # 2e8은 디딤돌이 가질 수 있는 최댓값
    min_ = 0
    max_ = 2e8

    while min_ <= max_:
        mid = (min_ + max_) // 2
        # mid명이 전부 밟을 경우 디딤돌이 사라지는지 확인하기 위해 zero_count 계산
        # 사라지는 디딤돌의 갯수
        zero_count = 0

        for s in stones:
            # mid명이 모두 밟고 지나갈수 있으면 zero_count 처음부터 다시 계산
            if s >= mid:
                zero_count = 0
            elif s < mid:
                zero_count += 1
                # 사라지는 디딤돌의 갯수가 한번에 건너뛸 수 있는 디딤돌의 칸수를 넘으면
                if zero_count >= k:
                    break
        # mid명은 너무 많으니까 1명 줄여서 다시 이분탐색
        if zero_count >= k:
            max_ = mid - 1
        # mid명이 모두 건너갈 수 있는 경우
        else:
            answer = mid
            min_ = mid + 1

    return answer