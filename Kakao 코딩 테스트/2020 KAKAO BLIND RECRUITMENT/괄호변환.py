def check(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return True
            stack.pop(-1)
    return False


def transform(s):
    left = 0
    right = 0
    u = ''
    v = ''
    result = ''
    if s == '':
        return s
    for idx, i in enumerate(s):
        if i == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = s[:idx + 1]
            v = s[idx + 1:]
            break

    if check(u):
        result += '('
        result += transform(v)
        result += ')'
        u = u[1:-1]
        for j in u:
            if j == '(':
                result += ')'
            else:
                result += '('

        return result
    else:
        u += transform(v)
        return u


def solution(p):
    answer = transform(p)

    return answer