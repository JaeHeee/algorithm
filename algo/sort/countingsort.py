count = [0]*5
numbers = [1,3,2,4,3,2,5,3,1,2,
           3,4,4,3,5,1,2,3,5,2,
           3,1,4,3,5,1,2,1,1,1]

for i in range(30):
    count[numbers[i]-1] += 1

for num, c in enumerate(count):
    for j in range(c):
        print(num+1, end=" ")