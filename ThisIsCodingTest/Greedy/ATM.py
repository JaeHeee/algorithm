# BAEKJOON ATM

N = int(input())

answer = 0
people = sorted(map(int, input().split()))

sum_ = 0
for p in people:
    sum_ += p
    answer += sum_

print(answer)
