def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    # prices 라는 스택에서 데이터가 모두 소멸될때까지 반복
    idx = -1
    while prices:
        p = prices.pop()
        # 스택이 비어있는 경우
        if stack==[]:
            stack.append(p)
            idx -= 1
        # 스택의 탑부터 차례대로 비교
        else:
            for i in range(-1,-len(stack)-1,-1):
                if p <= stack[i]:
                    answer[idx] += 1
                else:
                    answer[idx] += 1
                    break
            stack.append(p)
            idx-=1
            
    return answer