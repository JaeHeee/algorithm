from itertools import combinations

def solution(relation):
    answer = 0
    row_length = len(relation)
    col_relation = [[] for _ in range(len(relation[0]))]
    unique = []
    non_unique = []

    for r in relation:
        for i in range(len(r)):
            col_relation[i].append(r[i])

    for idx, c_r in enumerate(col_relation):
        if len(set(c_r)) == row_length:
            answer += 1
        else:
            non_unique.append(c_r)

    for i in range(2, len(non_unique) + 1):
        candidates = list(combinations(range(len(non_unique)), i))
        for cand in candidates:
            redundant = False
            for u in unique:
                if set(u).issubset(set(cand)):
                    redundant = True
                    break
            if redundant: continue

            check = []
            for j in range(row_length):
                check.append(tuple([non_unique[c][j] for c in cand]))

            if len(set(check)) == row_length:
                unique.append(cand)
                answer += 1

    return answer