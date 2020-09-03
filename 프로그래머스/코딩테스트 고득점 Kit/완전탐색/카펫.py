def solution(brown, yellow):
    # yellow의 가로, 세로
    w = 1
    h = 1

    while h <= w:
        if yellow % h ==0:
            w = yellow//h
            # 테두리를 계산한 것이 brown과 같은지
            if (w+h+2)*2 == brown:
                break
            else:
                h += 1
        else:
            h += 1

    return [w+2, h+2]



## max_time = 0.14ms