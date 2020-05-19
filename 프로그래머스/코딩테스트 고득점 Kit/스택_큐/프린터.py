def solution(priorities, location):
    answer = 0
    m = max(priorities)

    while True:
        wait = priorities.pop(0)
        if wait == m:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(wait)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return answer