#the Seven Dwarfs

dwarfs = []

for i in range(9):
    height = int(input(''))
    dwarfs.append(height)

dwarfs.sort()
memo = []

for i in range(8):
    check = 0
    for j in range(i,8):
        memo.append(dwarfs.pop(i))
        memo.append(dwarfs.pop(j))
        if sum(dwarfs) == 100:
            check = 1
            answer = dwarfs[:]
            break
        else:
            dwarfs += memo
            dwarfs.sort()
            del memo[:]
    if check == 1:
        break

for i in answer:
    print(i)
