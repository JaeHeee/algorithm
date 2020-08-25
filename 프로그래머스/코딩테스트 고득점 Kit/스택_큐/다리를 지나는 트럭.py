def solution(bridge_length, weight, truck_weights):
    answer = 0
    # bridge queue
    bridge = [0] * bridge_length
    bridge_weight = 0

    # 모든 트럭이 이동하면 종료
    while truck_weights:
        answer += 1
        # 다리의 맨 끝에서 빠져나갑니다.
        bridge_weight -= bridge.pop(0)
        # 트럭이 다리로 진입할 수 있는 경우
        if weight - bridge_weight >= truck_weights[0]:
            bridge_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    return answer + bridge_length