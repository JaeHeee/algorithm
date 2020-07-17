def solution(s):
    stack = []
    for i in s:
        if stack == []:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(i)

    if stack:
        return 0
    else:
        return 1