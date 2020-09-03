from itertools import permutations


def solution(paper):
    answer = 0
    # 숫자 조합들
    numbers = set()

    # numbers의 표현할 수 있는 모든 순열을 만듭니다.
    for i in range(1, len(paper) + 1):
        temp = list(permutations(paper, i))
        # 순열들을 합쳐서 숫자 조합으로 만듭니다.
        for t in temp:
            numbers.add(int(''.join(t)))

    # 에라토스테네스의 체
    max_ = max(numbers)
    sieve = [1] * (max_ + 1)

    for i in range(2, int(max_**0.5) + 1):
        if sieve[i] == 1:
            j=2
            while i*j <= max_:
                k = i*j
                j+=1
                sieve[k] = 0

    # 소수만 가져오기
    prime_numbers = [i for i in range(2, len(sieve)) if sieve[i] == 1]

    # numbers의 숫자가 소수인지 확인
    for n in numbers:
        if n in prime_numbers:
            answer += 1

    return answer

## max_time = 2364.02ms