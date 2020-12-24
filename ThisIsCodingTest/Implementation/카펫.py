# Progrmmers 카펫 문제

def solution(brown, yellow):
    w = 1
    h = 1

    while h <= w:
        if yellow % h ==0:
            w = yellow//h
            if (w+h+2)*2 == brown:
                break
            else:
                h += 1
        else:
            h += 1

    return [w+2, h+2]
