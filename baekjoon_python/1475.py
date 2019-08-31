#room number

N = input('')

numbers = ['0','1','2','3','4','5','6','7','8','9']
count = []

for number in numbers:
    count.append(N.count(number))

if count[6] == 0 and count[9] == 0:
    print(max(count))
elif count[6] != 0 or count[9] != 0:
    check = count[6] + count[9]
    if check % 2 ==0:
        check = check//2
        count[6]=0
        count[9]=0
    else:
        check = check//2+1
        count[6]=0
        count[9]=0
    if max(count)>=check:
        print(max(count))
    else:
        print(check)
