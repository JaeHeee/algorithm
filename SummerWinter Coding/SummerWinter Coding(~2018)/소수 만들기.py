from itertools import combinations

def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
    

def solution(nums):
    answer = 0

    num_com = list(combinations(nums, 3))

    for n in num_com:
        if is_prime(sum(n)):
            answer += 1

    return answer
