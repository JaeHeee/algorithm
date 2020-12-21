# 프로그래머스 큰 수 만들기 문제

def solution(number, k):
    stack = []

    for num in number:
        # 마지막 숫자보다 더 큰 숫자이고 ,제거할 숫자가 남아있으면 pop
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        stack.append(num)

    # 제거할 숫자가 남아있으면 pop
    while k > 0:
        stack.pop()
        k -= 1

    answer = "".join(stack)

    return answer
