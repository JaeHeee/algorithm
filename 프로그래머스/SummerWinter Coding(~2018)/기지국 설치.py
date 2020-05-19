def solution(n, stations, w):
    answer = 0
    start = 0
    r = 2*w + 1
    last_left = stations[-1] - (w + 1)
    
    for s in stations:
        left = s - (w + 1)
        right = s + w
        if left<1 and right>n:
            break
        if start <= left:
            answer += (left-start)//r
            if (left-start)%r:
                answer += 1
        start = right
    
    if start < n and last_left != start and start != 1:
        answer += (n-start)//r
        if (n-start)%r:
            answer += 1
                    
    return answer
