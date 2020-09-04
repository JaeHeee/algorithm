def solution(k, room_number):
    room = {}
    answer = []

    for i in room_number:
        num = i
        visit = [num]

        # 이미 배정된 방인 경우
        while num in room:
            num = room[num]
            visit.append(num)

        # 배정된 방 answer에 추가
        answer.append(num)

        # 배정된 방을 선택할 경우 다음으로 배정해줄 방 기록
        for j in visit:
            room[j] = num+1

    return answer