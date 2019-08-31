#ACM hotel

T = int(input(''))
floor = 0
room = 0

for i in range(T):
    H, W, N = map(int,input('').split())
    if N%H==0:
        floor = H
        if N//H < 10:
            room = N//H
            print(floor,end='')
            print(0,end='')
            print(room)
        else:
            room = N//H
            print(floor,end='')
            print(room)
    else:
        floor = N%H
        if N//H < 9:
            room = (N//H)+1
            print(floor,end='')
            print(0,end='')
            print(room)
        else:
            room = (N//H)+1
            print(floor,end='')
            print(room)
