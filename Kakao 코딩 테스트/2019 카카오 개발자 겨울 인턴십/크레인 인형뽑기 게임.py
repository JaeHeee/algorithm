def solution(board, moves):
    answer = 0
    basket = []
    check = 0
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                check = j[i-1]
                j[i-1] = 0
                break
            check = 0
        if basket == [] and check != 0:
            basket.append(check)
        elif basket != [] and basket[-1] == check:
            basket.pop(-1)
            answer += 2
        elif check != 0:
            basket.append(check)
    return answer
