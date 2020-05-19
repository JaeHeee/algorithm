def solution(clothes):
    answer = 1
    c_dict = {}
    for c in clothes:
        if c[1] in c_dict.keys():
            c_dict[c[1]] += 1
        else:
            c_dict[c[1]] = 1

    for v in c_dict.values():
        answer *= (v + 1)
    return answer - 1