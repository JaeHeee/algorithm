from math import sqrt

def solution(n):
    answer = 0
    if n%sqrt(n)==0:
        answer = (sqrt(n)+1)**2
    else:
        answer = -1
    return answer