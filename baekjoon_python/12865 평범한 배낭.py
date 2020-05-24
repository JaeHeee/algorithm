N, K = map(int, input().split())
W = []
V = []
dp_v = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)


for i in range(1, N+1):
    for j in range(1, K+1):
        if(j < W[i-1]):
            dp_v[i][j] = dp_v[i-1][j]
        else:
            dp_v[i][j] = max(dp_v[i-1][j], dp_v[i-1][j-W[i-1]] + V[i-1])
print(dp_v[N][K])

