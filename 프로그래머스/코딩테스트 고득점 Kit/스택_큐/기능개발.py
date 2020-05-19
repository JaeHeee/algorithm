def solution(progresses, speeds):
    answer = []
    remain = []
    stack = []
    for p, s in zip(progresses, speeds):
        if (100 - p) % s:
            remain.append((100 - p) // s + 1)
        else:
            remain.append((100 - p) // s)

    while remain:
        if stack == []:
            stack.append(remain.pop(0))
        else:
            if remain[0] <= stack[0]:
                stack.append(remain.pop(0))
            else:
                answer.append(len(stack))
                stack = []
    answer.append(len(stack))

    return answer