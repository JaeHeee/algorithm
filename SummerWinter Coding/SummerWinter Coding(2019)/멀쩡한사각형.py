import math

def solution(w,h):
    answer = 0
    
    g = math.gcd(w,h)
    
    answer = w*h - g*(w//g + h//g - 1)   
    
    
    return answer
