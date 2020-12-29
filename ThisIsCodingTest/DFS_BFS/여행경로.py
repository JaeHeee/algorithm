# Programmers 여행경로

from collections import defaultdict

def solution(tickets):
    answer = [tickets[0][0]]

    ticket_dict = defaultdict(list)

    for start, end in tickets:
        ticket_dict[start].append(end)

    for k in ticket_dict.keys():
        ticket_dict[k].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if len(ticket_dict[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(ticket_dict[top].pop())

    answer = path[::-1]

    return answer
