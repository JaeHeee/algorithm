# BAEKJOON 홀수

numbers = []

for _ in range(7):
    num = int(input())
    if num % 2:
        numbers.append(num)

numbers.sort()

if numbers:
    print(sum(numbers))
    print(numbers[0])
else:
    print(-1)
