T = int(input())

def make_pizza():
    oven = []
    number = 1

    for _ in range(N):
        oven.append([cheeze[0], number])
        cheeze.pop(0)
        number += 1

    while len(oven) != 1:
        oven[0][0] = oven[0][0] // 2

        if oven[0][0] == 0:
            oven.pop(0)
            if len(cheeze) != 0:
                oven.append([cheeze[0], number])
                cheeze.pop(0)
                number += 1
        else:
            oven.append(oven.pop(0))

    return oven[0][1]

for i in range(T):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))
    result = make_pizza()

    print("#%d %d" % (i+1, result))
