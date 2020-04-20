T = int(input())

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
check = []
for i in range(1<<12):
    sub = []
    for j in range(12):
        if i & (1<<j):
            sub.append(number[j])
    check.append(sub)

for i in range(T):
    count = 0
    N, K = map(int, input().split())

    for c in check:
        if len(c)==N and sum(c)==K:
            count +=1

    print("#%d %d" % (i+1, count))
