# Z

N, r, c = map(int,input('').split())

def search(N,r,c):
    if N==0:
        return 0
    if r < 2**(N-1):
        if c < 2**(N-1):## 1사분면
            return search(N-1,r,c)
        else:## 2사분면
            return 2**(2*N-2) + search(N-1,r,c-2**(N-1))
    else:
        if c < 2**(N-1):##3사분면
            return 2**(2*N-1) + search(N-1,r-2**(N-1),c)
        else:##4사분면
            return 3*2**(2*N-2) + search(N-1,r-2**(N-1),c-2**(N-1))

print(search(N,r,c))
