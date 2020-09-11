def solution(board, moves):
    answer = 0
    basket = []
    check = 0

    for i in moves:
        for j in board:
            # 해당 칸이 빈 공간아니면 인형뽑기
            if j[i-1] != 0:
                check = j[i-1]
                j[i-1] = 0
                break
            check = 0
        # 빈 바구니에 뽑은 인형 넣기
        if basket == [] and check != 0:
            basket.append(check)
        # 바구니 제일 위에 같은 인형 있는 경우
        elif basket != [] and basket[-1] == check:
            basket.pop(-1)
            answer += 2
        elif check != 0:
            basket.append(check)

    return answer