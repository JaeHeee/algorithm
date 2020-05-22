def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    count = [[0,1],[0,2],[0,3]]
    a,b,c = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == one[a]:
            count[0][0] += 1
        if answers[i] == two[b]:
            count[1][0] += 1
        if answers[i] == three[c]:
            count[2][0] += 1
        if a + 1 == 5:
            a = 0
        else:
            a+=1
        if b + 1 == 8:
            b = 0
        else:
            b+=1
        if c + 1 == 10:
            c = 0
        else:
            c+=1

    count.sort()
    if count[0][0] == count[2][0]:
        return [1,2,3]
    elif count[2][0] == count [1][0]:
        answer = [count[2][1],count[1][1]]
        answer.sort()
        return answer
    else:
        return [count[2][1]]
