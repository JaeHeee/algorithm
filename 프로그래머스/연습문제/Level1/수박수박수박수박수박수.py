def solution(n):
    answer = "수박"
    if n % 2 == 0:
        answer *= n // 2
    else:
        answer *= (n // 2)
        answer += "수"

    return answer