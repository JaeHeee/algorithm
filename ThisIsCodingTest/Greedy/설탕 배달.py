# BAEKJOON 설탕 배달 문제


N = int(input())

answer = 0

for i in range(0, N//3+1):
    sugar = N - 3*i
    if sugar % 5 == 0:
        answer = i + sugar//5
        break
if answer:
    print(answer)
else:
    print(-1)
