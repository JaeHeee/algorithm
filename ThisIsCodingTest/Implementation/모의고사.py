# Programmers 모의고사 문제
from collections import defaultdict

def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_idx, two_idx, three_idx = 0, 0, 0

    count = defaultdict(int)
    
    for a in answers:
        if a == one[one_idx]:
            count[1] += 1
        if a == two[two_idx]:
            count[2] += 1
        if a == three[three_idx]:
            count[3] += 1
        
        if one_idx + 1 == len(one):
            one_idx = 0
        else:
            one_idx += 1
        if two_idx + 1 == len(two):
            two_idx = 0
        else:
            two_idx += 1
        if three_idx + 1 == len(three):
            three_idx = 0
        else:
            three_idx += 1
            
    count_list = list(count.items())
    count_list.sort(key = lambda x : x[1], reverse = True)
    
    for c in count_list:
        if answer:
            if c[1] == count[answer[-1]]:
                answer.append(c[0])
            else:
                break
        else:
            answer.append(c[0])
    
    return sorted(answer)
