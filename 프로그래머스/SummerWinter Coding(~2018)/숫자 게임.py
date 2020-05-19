def solution(A, B):
    answer = 0
    
    if max(B) <= min (A):
        return answer
    
    if max(A) != min (A):
        A.sort(reverse=True)
        B.sort(reverse=True)
    for a in A:
        for b in B:
            if a < b:
                B.pop(B.index(b))
                answer += 1
                break
                
    return answer
