T = int(input())

for i in range(T):
    N, M, L = map(int, input().split())
    numbers = list(map(int, input().split()))
    add_list = []
    for j in range(M):
        idx, num = map(int, input().split())
        add_list.append([idx, num])

    for k in add_list:
        temp = numbers[:k[0]]
        temp.append(k[1])
        numbers = temp + numbers[k[0]:]

    print("#%d %d" % (i+1, numbers[L]))
