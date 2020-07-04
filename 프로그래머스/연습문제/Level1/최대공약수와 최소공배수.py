def gcd(n, m):
    if n > m:
        n, m = m, n

    while n != 0:
        a = m % n
        m = n
        n = a

    return m


def solution(n, m):
    answer = [gcd(n, m), n * m // gcd(n, m)]
    return answer