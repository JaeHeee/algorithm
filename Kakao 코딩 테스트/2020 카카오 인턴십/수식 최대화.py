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
            if e in operators:  # operator 면 추가
                exp.append(e)
            elif exp[-1] not in operators:  # operator 아니면 문자열 합쳐주기
                exp[-1] += e
            elif exp[-1] in operators:
                exp.append(e)

    # 모든 operator 순열 만들기
    operators = list(permutations(operators, 3))

    for operator in operators:
        data = exp[:]
        stack = []
        for op in operator:
            while data:
                d = data.pop(0)
                if d == op:
                    # 스택에 있는 수와 data의 수 꺼내서 op로 연산
                    cal = operation(stack.pop(-1), data.pop(0), op)
                    stack.append(cal)
                else:
                    stack.append(d)
            data = stack
            stack = []
        answer.append(abs(int(data[0])))

    return max(answer)

solution("100-200*300-500+20")