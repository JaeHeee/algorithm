def solution(s):
    answer = True
    stack = []

    for i in s:
        if stack == []:
            stack.append(i)
        else:
            if i == '(':
                stack.append(i)
            else:
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    stack.append(i)

    if stack:
        return False
    else:
        return True