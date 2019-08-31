#check
def GCD(M,N):
    if M%N==0:
        return N
    return GCD(N,M%N)

N = int(input(''))
numbers = []
m = []

for i in range(N):
    number = int(input(''))
    numbers.append(number)
numbers.sort()

g = numbers[1]-numbers[0]
for j in range(2,N):
    g = GCD(g,numbers[j]-numbers[j-1])

k=1
while k*k <= g:
    if g%k==0:
        m.append(k)
        if g//k != k:
            m.append(g//k)
    k+=1

m.remove(1)
m.sort()

for value in m:
    print(value,end=' ')
