def solution(record):
    answer = []
    records = dict()
    result = []

    for r in record:
        temp = r.split(' ')

        if temp[0] == 'Leave':
            result.append([temp[1], "님이 나갔습니다."])
        elif temp[0] == 'Enter':
            records[temp[1]] = temp[2] # key=유저 아이디 value=이름
            result.append([temp[1], "님이 들어왔습니다."])
        else:
            records[temp[1]] = temp[2]

    for r in result:
        answer.append(records[r[0]] + r[1])

    return answer
