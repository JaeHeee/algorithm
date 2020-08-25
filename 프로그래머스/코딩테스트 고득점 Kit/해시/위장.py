def solution(clothes):
    answer = 1
    clothes_d = {}
    
    # key = 의상의 종류, value = 의상의 이름
    for c in clothes:
        if c[1] in clothes_d.keys():
            clothes_d[c[1]].append(c[0])
        else:
            clothes_d[c[1]] = [c[0]]

    # 아무것도 입지 않는 상태를 포함하여 가능한 경우의 수를 구합니다.
    for v in clothes_d.values():
        answer *= (len(v)+1)

    return answer - 1
