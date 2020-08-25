def solution(citations):
    answer = 0
    # H-index가 될수 있는 최댔값은 n
    n = len(citations)
    citations.sort()
    
    for i, c in enumerate(citations):
        # i = 나머지 논문의 수, n-i = c번 이상 인용된 논문의 수
        if n-i <= c:
            return n-i
        
        
    return answer