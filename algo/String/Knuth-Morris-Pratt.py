# 접두사와 접미사의 개념을 활용하여 반복되는 연산을 얼마나 줄일 수 있는지 판별
# 접두사와 접미사를 늘려가며 비교하다가
# 일치하지 않는 경우가 발생하면 일치했던 부분까지 되돌아가서 다시 검사하는 방식
# 접두사와 접미사가 일치하는 길이를 찾아낸다.

def makeTable(pattern):
    pattern_size = len(pattern)
    table = [0]*pattern_size

    # 일치하지 않으면 i만 증가 일치하면 i, j 둘다 증가
    j = 0
    for i in range(1, pattern_size):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    # 해당 지점까지의 접두사 접미사가 일치하는 최대길이가 table의 값
    return table

def KMP(parent, pattern):
    table = makeTable(pattern)
    parent_size = len(parent)
    pattern_size = len(pattern)

    # 일치하지 않는 경우 table을 이용해서 해당 위치부터 다시 확인
    j = 0
    for i in range(parent_size):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]

        if parent[i] == pattern[j]:
            if j == pattern_size - 1:
                print(i-pattern_size+2, "번째")
                j = table[j]
            else:
                j += 1

parent = "ababacabacaabacaaba"
pattern = "abacaaba"

KMP(parent, pattern)