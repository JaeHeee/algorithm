def solution(tickets):
    answer = [tickets[0][0]]
    ticket_dict = dict()

    for (start, end) in tickets:
        ticket_dict[start] = ticket_dict.get(start, []) + [end]

    for k in ticket_dict.keys():
        ticket_dict[k].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if top not in ticket_dict or len(ticket_dict[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(ticket_dict[top][-1])
            ticket_dict[top] = ticket_dict[top][:-1]

    answer = path[::-1]

    return answer