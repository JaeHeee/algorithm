from itertools import permutations


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def solution(expression):
    operators = ['+', '-', '*']
    exp = []
    answer = []

    for e in expression:
        if exp == []:
            exp.append(e)
        else:
            if e in operators:
                exp.append(e)
            elif exp[-1] not in operators:
                exp[-1] += e
            elif exp[-1] in operators:
                exp.append(e)

    operators = list(permutations(operators, 3))

    for operator in operators:
        data = exp[:]
        stack = []
        for op in operator:
            while data:
                d = data.pop(0)
                if d == op:
                    cal = operation(stack.pop(-1), data.pop(0), op)
                    stack.append(cal)
                else:
                    stack.append(d)
            data = stack
            stack = []
        answer.append(abs(int(data[0])))

    return max(answer)