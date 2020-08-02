def solution(s):
    answer = len(s)
    # 몇개의 단위로 나눌것인지
    for i in range(1, len(s)):
        stack = []
        pos = 0
        count = 0
        temp = ''

        # 단위별로 문자열 확인
        while pos + i < len(s) + 1:
            # 스택이 비어있는 경우
            if not stack:
                stack.append(s[pos:pos + i])
                count += 1
                pos += i
            # 이전의 문자열과 현재의 문자열이 같은 경우
            elif stack[-1] == s[pos:pos + i]:
                stack.append(s[pos:pos + i])
                count += 1
                pos += i
            # 이전의 문자열과 현재의 문자열이 다른 경우
            elif stack[-1] != s[pos:pos + i]:
                if count > 1:
                    temp += str(count)
                temp += stack[-1]
                stack = []
                stack.append(s[pos:pos + i])
                count = 1
                pos += i
        # 스택에 남아있는 문자열을 붙여준다.
        if len(stack) == 1:
            temp += stack.pop()
        elif len(stack) > 1:
            temp += (str(len(stack)) + stack[-1])

        # 위의 과정을 거치고 남아있는 문자열을 붙여준다.
        if pos <= len(s) - 1:
            temp += s[pos:]

        # 문자열중 가장 짧은 것 찾아내기
        answer = min(answer, len(temp))
    return answer