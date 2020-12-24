# Programmers 소수 찾기 문제

from itertools import permutations

def solution(paper):
    answer = 0
    numbers = set()

    for i in range(1, len(paper) + 1):
        temp = list(permutations(paper, i))
        for t in temp:
            numbers.add(int(''.join(t)))

    max_ = max(numbers)
    sieve = [1] * (max_+1)

    for i in range(2, int(max_**0.5) + 1):
        if sieve[i] == 1:
            j = 2
            while i*j <= max_:
                k = i*j
                j += 1
                sieve[k] = 0

    prime_numbers = [i for i in range(2, len(sieve)) if sieve[i] == 1]

    for n in numbers:
        if n in prime_numbers:
            answer += 1

    return answer
