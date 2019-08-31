#stairs

N = int(input(''))
stairs=[]

for i in range(N):
    s = int(input(''))
    stairs.insert(0,s)

def step(N):
    if N==1:
        return stairs[0]
    elif N==2:
        return stairs[0]+stairs[1]
    else:
        dp=[]
        dp.append([0,0,0])
        dp.append([stairs[0],stairs[0]+stairs[1],0])
        dp.append([stairs[0]+stairs[1],0,stairs[0]+stairs[2]])
        if N >3:
            for i in range(3,N):
                dp.append([0,0,0])
                dp[i][0] = max(dp[i-1][1],dp[i-1][2])
                dp[i][1] = dp[i-1][2]+ stairs[i]
                dp[i][2] = max(dp[i-2][1],dp[i-2][2])+ stairs[i]
    return max(dp[N-1][0],dp[N-1][1],dp[N-1][2])

print(step(N))
