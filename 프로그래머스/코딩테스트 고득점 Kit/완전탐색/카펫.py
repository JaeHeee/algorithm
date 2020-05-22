def solution(brown, yellow):
    row = 1
    col = 1
    while row >= col:
        if yellow % col == 0:
            row = yellow // col
            if (row + col + 2) * 2 == brown:
                break
            else:
                col += 1
        else:
            col += 1
    answer = [row + 2, col + 2]

    return answer