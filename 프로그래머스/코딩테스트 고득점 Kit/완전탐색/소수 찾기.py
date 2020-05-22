from itertools import permutations


def solution(numbers):
    answer = 0
    prime = list(numbers)
    for i in range(2, len(numbers) + 1):
        temp = list(permutations(numbers, i))
        for t in temp:
            prime.append(''.join(t))
    prime_set = set([int(p) for p in prime])

    sieve = [1] * (max(prime_set) + 1)
    for j in range(2, int(max(prime_set) ** 0.5) + 1):
        if sieve[j] == 1:
            for k in range(j + j, max(prime_set) + 1, j):
                sieve[k] = 0
    prime_numbers = [n for n in range(2, max(prime_set) + 1) if sieve[n] == 1]
    for p in prime_set:
        if p in prime_numbers:
            answer += 1

    return answer