T = int(input())

for i in range(T):
    str1 = input()
    str2 = input()

    str1 = set(str1)
    str1_dict = { s : 0 for s in str1}

    for s1 in str1:
        for s2 in str2:
            if s1 == s2:
                str1_dict[s1] += 1

    print("#%d %d" % (i+1, max(str1_dict.values())))
