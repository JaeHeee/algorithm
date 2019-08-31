# wine

N = int(input(''))
wines = []

for i in range(N):
    wine = int(input(''))
    wines.append(wine)

def drink(N):
    dp=[]
    if N == 1:
        dp.append([0,wines[0],0])
    elif N == 2:
        dp.append([0,wines[0],0])
        dp.append([wines[0], wines[1],wines[0]+wines[1]])
    else:
        dp.append([0,wines[0],0])
        dp.append([wines[0], wines[1],wines[0]+wines[1]])
        for i in range(2,N):
            dp.append([0,0,0])
            dp[i][0] = max(dp[i-1][0],max(dp[i-1][1],dp[i-1][2]))
            dp[i][1] = dp[i-1][0] + wines[i]
            dp[i][2] = dp[i-1][1] + wines[i]
    return max(dp[N-1][0],dp[N-1][1],dp[N-1][2])

print(drink(N))
