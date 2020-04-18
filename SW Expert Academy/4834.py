T = int(input())

for i in range(T):
    check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = 0
    N = int(input())
    number = list(input())
    number = [int(j) for j in number]

    for num in number:
        check[num] += 1

    for k in range(9,-1,-1):
        if max(check) == check[k]:
            result = k
            break

    print("#%d %d %d" % (i+1, result, max(check)))
