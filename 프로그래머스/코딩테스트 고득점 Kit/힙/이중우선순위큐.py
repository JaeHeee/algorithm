def solution(operations):
    answer = [0, 0]
    queue = []
    for op in operations:
        a = op.split(' ')
        if a[0] == 'I':
            queue.append(int(a[1]))
        else:
            if a[1] == '1' and queue:
                queue.remove(max(queue))
            elif a[1] == '-1' and queue:
                queue.remove(min(queue))
    if queue:
        answer = [max(queue), min(queue)]

    return answer