def solution(k, room_number):
    room = {}
    answer = []
    for i in room_number:
        num = i
        visit = [num]
        while num in room:
            num = room[num]
            visit.append(num)
        answer.append(num)
        for j in visit:
            room[j] = num+1
    return answer

