#Goldbach's conjecture

def prime(number):
    k = 2
    while k*k <= number:
        if number%k==0:
            return 0
        k+=1
    return True

T = int(input())
even = []

for i in range(T):
    e = int(input())
    even.append(e)

for j in even:
    k = int(j/2)
    while k>=2:
        if prime(k) and prime(j-k):
            print(k,end=' ')
            print(j-k)
            break
        k -= 1
