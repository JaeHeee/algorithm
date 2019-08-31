#coin 0

N, K = map(int,(input('').split()))
coins = [[],[]]
for i in range(N):
    coin = int(input(''))
    if coin <= K:
        coins[0].append(coin)
        coins[1].append(0)

if N==1:
    print(K)
else:
    j = -1
    while K>0:
        while K>=coins[0][j]:
            count = K//coins[0][j]
            K -= coins[0][j]*count
            coins[1][j] += count
        j -= 1
    print(sum(coins[1]))
