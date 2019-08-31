#Intelligent train

passenger = [0,0,0,0]
for i in range(4):
    decrease, increase = map(int,input('').split(' '))
    if i==0:
        passenger[i] += (increase - decrease)
    else:
        passenger[i] = passenger[i-1] + (increase - decrease)

print(max(passenger))
