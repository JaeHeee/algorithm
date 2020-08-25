def solution(progresses, speeds):
    answer = []
    remain = []
    stack = []
    # 작업 완료까지 나은 날짜 수를 remain에 넣습니다.
    for p, s in zip(progresses, speeds):
        if (100-p)%s:
            remain.append((100-p)//s+1)
        else:
            remain.append((100-p)//s)
    
    # 스택의 사이즈 = 한번 배포할 때 완성되는 기능의 수
    while remain:
        if stack==[]:
            stack.append(remain.pop(0))
        else:
            # 스택에 있는 날짜가 더 크면 스택에 추가
            if remain[0] <= stack[0]:
                stack.append(remain.pop(0))
            # 스택에 있는 날짜가 더 작으면 스택을 초기화
            else:
                answer.append(len(stack))
                stack = []
    answer.append(len(stack))
                        
    return answer