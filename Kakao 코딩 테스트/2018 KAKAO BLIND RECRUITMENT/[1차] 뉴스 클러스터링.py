def solution(str1, str2):
    answer = 0
    int_ = 0
    uni_ = 0

    multilist1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    multilist2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    multiset1 = set(multilist1)
    multiset2 = set(multilist2)
    multiint = multiset1.intersection(multiset2)
    multiuni = multiset1.union(multiset2)

    for i in multiint:
        int1 = multilist1.count(i)
        int2 = multilist2.count(i)
        int_ += min(int1, int2)

    for u in multiuni:
        uni1 = multilist1.count(u)
        uni2 = multilist2.count(u)
        uni_ += max(uni1, uni2)

    if uni_ == 0:
        answer = 1
    else:
        answer = int_ / uni_

    return int(answer * 65536)