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
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if s == '':
        return s

    for idx, i in enumerate(s):
        if i == '(':
            left += 1
        else:
            right += 1
        # 균형잡힌 문자열 인지 확인하고 맞으면, u를 균형잡힌 문자열로 나머지는 v로 분리
        # 균형잡힌 문자열 = '(' 와 ')'의 개수가 같은 문자열
        if left == right:
            u = s[:idx + 1]
            v = s[idx + 1:]
            break
    # u가 올바른 문자열인지 확인
    # 올바른 문자열이 아닌경우
    if check(u):
        result += '('
        result += transform(v)
        result += ')'
        # u의 첫 번째와 마지막 문자 제거하고, 나머지 문자열의 괄호 방향 뒤집어서 뒤에 붙입니다.
        u = u[1:-1]
        for j in u:
            if j == '(':
                result += ')'
            else:
                result += '('
        return result
    # 올바른 문자열인 경우
    else:
        u += transform(v)
        return u


def solution(p):
    answer = transform(p)

    return answer