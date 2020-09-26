number = 100000
sieve = [0]*100001


def primeNumberSieve():
    for i in range(2, number+1):
        sieve[i] = i

    for i in range(2, number+1):
        if sieve[i] == 0:
            continue
        for j in range(i+i, number+1, i):
            sieve[j]=0

    for i in range(2, number+1):
        if sieve[i] != 0:
            print(sieve[i])

primeNumberSieve()