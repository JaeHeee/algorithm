#prime numbers

def prime(number):
    k = 2
    while k*k <= number:
        if number%k==0:
            return 0
        k+=1
    return True

M,N = map(int,input().split())

for i in range(M,N+1):
    if prime(i) and i != 1:
        print(i)
