T = int(input())

for i in range(T):
    forth = list(map(str, input().split()))
    numbers = []

    for f in forth:
        if f.isdecimal():
            numbers.append(int(f))
        elif len(numbers) == 0:
            result = 'error'
            break
        elif f == '.':
            result = numbers.pop()
        else:
            num1 = numbers.pop()
            if len(numbers) == 0:
                result = 'error'
                break
            num2 = numbers.pop()
            if f == '+':
                cal = num2 + num1
            elif f == '-':
                cal = num2 - num1
            elif f == '/':
                cal = num2//num1
            elif f == '*':
                cal = num2 * num1
            numbers.append(cal)

    if result == 'error' or len(numbers) >= 1:
        print("#%d %s" % (i+1, 'error'))
    else:
        print("#%d %d" % (i + 1, result))

