#GCD & LCM
def GCD(M,N):
    if M%N==0:
        return N
    return GCD(N,M%N)

def LCM(M,N):
    return int(M*N/GCD(M,N))

M, N = map(int,input('').split())

print(GCD(max(M,N),min(M,N)))
print(LCM(max(M,N),min(M,N)))
