T = int(input())


def win(a, b):
    if (cards[a-1] == 1 and cards[b-1] == 2) or (cards[a-1] == 2 and cards[b-1] == 3) or (cards[a-1] == 3 and cards[b-1] == 1):
        return b
    else:
        return a


def finder(s, e):
    if s == e:
        return s

    return win(finder(s, (s+e)//2), finder((s+e)//2 + 1, e))


for i in range(T):
    N = int(input())
    cards = list(map(int, input().split()))

    result = finder(1, N)

    print("#%d %d" % (i + 1, result))

