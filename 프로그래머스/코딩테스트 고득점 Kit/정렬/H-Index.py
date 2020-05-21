def solution(citations):
    answer = 0
    max_ = max(citations)

    for i in range(max_ + 1):
        count = 0
        for c in citations:
            if c >= i:
                count += 1
        if count >= i:
            answer = max(answer, i)

    return answer