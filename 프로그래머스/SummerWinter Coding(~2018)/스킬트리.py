def solution(skill, skill_trees):
    answer = 0
    check = True
    
    for tree in skill_trees:
        temp = []
        check = True
        for t in tree:
            if t in skill:
                temp.append(t)
                
        for i in range(len(temp)):
            if temp[i] != skill[i]:
                check = False
                break
                
        if check is True:
            answer += 1
                
    return answer
