def solution(s):
    l = len(s)
    if l == 4 or l == 6:
        answer = s.isdigit()
    else:
        return False

    return answer