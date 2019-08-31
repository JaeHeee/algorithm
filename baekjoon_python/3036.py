#ring

def GCD(M,N):
    if M%N==0:
        return N
    return GCD(N,M%N)

N = int(input(''))
ring = list(map(int,input('').split()))

for i in range(1,N):
    g = GCD(ring[0],ring[i])
    print(ring[0]//g,end='')
    print('/',end='')
    print(ring[i]//g)
