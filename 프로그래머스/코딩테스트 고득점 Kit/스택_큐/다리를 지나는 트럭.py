def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length
    sum_q = 0
    while q:
        answer += 1
        sum_q -= q.pop(0)
        if truck_weights:
            if sum_q + truck_weights[0] <= weight:
                sum_q += truck_weights[0]
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return answer