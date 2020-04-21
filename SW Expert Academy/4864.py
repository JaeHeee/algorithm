T = int(input())

for i in range(T):
    check = 0

    str1 = input()
    str2 = input()

    if str1 in str2:
        check = 1

    print("#%d %d" % (i+1, check))
