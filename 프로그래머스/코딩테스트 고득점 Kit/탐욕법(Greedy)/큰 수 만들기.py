def solution(number, k):
    stack = []

    # 먼저 stack의 top이 새로 stack에 들어갈 숫자보다 작으면 제거
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    # 제거할 수가 남았을때 뒤에서부터 제거
    while k > 0:
        stack.pop()
        k -= 1

    answer = "".join(stack)

    return answer