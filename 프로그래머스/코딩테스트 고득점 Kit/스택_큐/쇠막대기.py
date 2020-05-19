def solution(arrangement):
    answer = 0
    sticks = 0
    rasor = arrangement.replace('()','0')

    for i in rasor:
        if i == '(':
            sticks += 1
        elif i =='0':
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer
