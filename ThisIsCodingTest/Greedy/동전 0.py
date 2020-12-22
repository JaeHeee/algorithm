# BAEKJOON 동전 0

N, K = map(int, input().split())

answer = 0
coins = []

for _ in range(N):
    coin = int(input())
    coins.append(coin)

while K:
    for coin in coins[::-1]:
        if coin <= K:
            answer += (K//coin)
            K %= coin
        else: continue

print(answer)
