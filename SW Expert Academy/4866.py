T = int(input())

for i in range(T):
    parentheses = {
        '(': ')',
        ')': '(',
        '{': '}',
        '}': '{'
    }
    stack = []
    words = input()
    check = 1

    for w in words:
        if w == '(' or w == '{':
            stack.append(w)
        elif w == ')' or w == '}':
            if len(stack) == 0:
                check=0
                break
            elif parentheses[w] == stack[-1]:
                stack.pop()
            else:
                stack.append(w)

    if len(stack)>0:
        check = 0

    print("#%d %s" % (i+1, check))
