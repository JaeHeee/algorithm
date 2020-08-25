def solution(priorities, location):
    answer = 0
    
    while True:
        max_ = max(priorities)
        check = priorities.pop(0)
        # 인쇄 대기목록의 가장 앞에 있는 문서가 우선순위가 가장 큰지 확인
        if check == max_:
            answer += 1
            # 요청한 문서라면 리턴
            if location==0:
                return answer
            else:
                location -= 1
        # 우선순위가 가장 크지 않다면 대기목록의 마지막으로 보냅니다.
        else:
            priorities.append(check)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1