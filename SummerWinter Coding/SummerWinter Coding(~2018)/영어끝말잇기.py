def solution(n, words):
    answer = []
    check = True
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            answer = [(i+1)%n+1, (i+1)//n + 1 ]
            check = False
            break
        elif words[i+1] in words[:i+1]:
            answer = [(i+1)%n+1, (i+1)//n + 1]
            check = False
            break
        
    if check is True:
        answer = [0, 0]
        

    return answer
