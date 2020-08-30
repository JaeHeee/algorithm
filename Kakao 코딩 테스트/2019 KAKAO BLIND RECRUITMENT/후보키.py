from itertools import combinations

def solution(relation):
    answer = 0
    row_length = len(relation)
    col_relation = [[] for _ in range(len(relation[0]))]
    unique = []
    non_unique = []

    # column 별 리스트
    for r in relation:
        for i in range(len(r)):
            col_relation[i].append(r[i])

    # column list 만으로 후보키가 될 수 있는지 확인
    for idx, c_r in enumerate(col_relation):
        if len(set(c_r)) == row_length:
            answer += 1
        else:
            non_unique.append(c_r)

    for i in range(2, len(non_unique) + 1):
        # non_unique에 있는 것들로 후보키 조합 만들기
        candidates = list(combinations(range(len(non_unique)), i))
        for cand in candidates:
            redundant = False
            for u in unique:
                # 최소성 기준 만족하는지 확인
                if set(u).issubset(set(cand)):
                    redundant = True
                    break
            if redundant: continue

            # 위에서 만든 후보키 조합 이용해서 실제로 릴레이션 만들어보기
            check = []
            for j in range(row_length):
                check.append(tuple([non_unique[c][j] for c in cand]))

            # 후보키에 들어가도 되는지 확인
            if len(set(check)) == row_length:
                unique.append(cand)
                answer += 1

    return answer