#sortinside

N = input()
numbers = []

for i in range(len(N)):
    numbers.append(N[i])

numbers.sort()

for j in range(-1,-len(numbers)-1,-1):
    print(numbers[j],end='')
