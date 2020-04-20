T = int(input())

for i in range(T):
    A = 0
    B = 0
    P, PA, PB = map(int, input().split())

    la, lb = 1, 1
    ra, rb = P, P
    ca = int((la + ra)/2)
    cb = int((lb + rb) / 2)

    while(ca != PA):
        if PA > ca:
            la = ca
            ca = int((la + ra)/2)
            A += 1
        else:
            ra = ca
            ca = int((la + ra) / 2)
            A += 1

    while (cb != PB):
        if PB > cb:
            lb = cb
            cb = int((lb + rb) / 2)
            B += 1
        else:
            rb = cb
            cb = int((lb + rb) / 2)
            B += 1
    
    if A==B:
        print("#%d 0" % (i+1))
    elif A < B:
        print("#%d A" % (i + 1))
    else:
        print("#%d B" % (i + 1))
