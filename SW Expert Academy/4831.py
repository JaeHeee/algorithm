T = int(input())

for i in range(T):
    count = 0
    position = 0
    K, N, M = map(int, input().split(" "))

    charge = list(map(int,input().split(" ")))

    while position < N:
        for j in range(K, 0, -1):
            if position+j == N:
                position = N
                break
            if position+j in charge:
                position += j
                count += 1
                break
            elif position+j not in charge and j == 1:
                count = 0
                position = N
                break



    print("#%d %d" % (i+1, count))
