T = int(input())

for i in range(T):
    stack = []
    words = input()

    for w in words:
        if len(stack) == 0:
            stack.append(w)
        elif stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)

    print("#%d %s" % (i+1, len(stack)))
