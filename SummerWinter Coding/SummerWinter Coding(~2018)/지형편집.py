def solution(land, P, Q):
    answer = -1
    N = len(land)
    v = []
    for i in range(N):
        for j in range(N):
            v.append(land[i][j])
    v.sort()

    temp = 0
    for i in range(len(v)):
        temp += (v[i]-v[0])*Q
    answer = temp

    for i in range(1, len(v)):
        down = i
        up = len(v) - i
        temp += down*(v[i]-v[i-1])*P
        temp -= up*(v[i] - v[i-1])*Q
        if answer > temp:
            answer = temp
    return answer