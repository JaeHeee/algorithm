#rope

N = int(input(''))
ropes = []

for i in range(N):
    weight = int(input(''))
    ropes.append(weight)

ropes.sort()

count = N
for j in range(N):
    ropes[j] *= count
    count -=1

print(max(ropes))
