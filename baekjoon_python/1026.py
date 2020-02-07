S=0
N = int(input(''))

A = list(map(int,input('').split()))
B = list(map(int,input('').split()))

A.sort()
B.sort()

for i in range(N):
    S += A[i]*B[N-1-i]

print(S)
