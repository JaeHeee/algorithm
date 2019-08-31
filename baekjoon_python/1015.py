#sequence sort

N = int(input(''))
A = list(map(int,input('').split()))

B = A[:]
B.sort()

P = []
for i in range(N):
    P.append(B.index(A[i]))
    B[B.index(A[i])] = -1

for i in range(N):
    print(P[i],end=' ')
