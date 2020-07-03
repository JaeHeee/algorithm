def solution(s, n):
    answer = ''
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = [u.lower() for u in upper]

    for i in s:
        if i in upper:
            answer += upper[upper.index(i) + n - 26]
        elif i == ' ':
            answer += i
        else:
            answer += lower[lower.index(i) + n - 26]

    return answer