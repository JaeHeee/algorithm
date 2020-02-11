N = int(input(''))
count = 0

for i in range(0,N):
    check = []
    word = input('')
    if(len(word) == 1):
        count += 1
    else:
        for s in word:
            if(s not in check):
                check.append(s)
            elif(s in check and s != check[-1]):
                continue
            elif(s in check):
                check.append(s)
    if(len(word) == len(check)):
        count+=1
                

print(count)
