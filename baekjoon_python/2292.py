#honeycomb

N = int(input(''))

if N == 1:
    print(1)
else:
    for i in range(1,N+1):
        if 1+6*(i*(i+1))/2 >= N:
            print(i+1)
            break
