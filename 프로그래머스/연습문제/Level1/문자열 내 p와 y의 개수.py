def solution(s):
    s_lower = s.lower()
    p_count = s_lower.count('p')
    y_count = s_lower.count('y')

    if p_count == y_count and p_count == 0:
        return True
    elif p_count == y_count:
        return True
    else:
        return False