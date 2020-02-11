test = int(input(''))

for i in range(0,test):
    iter , str = input('').split()
    result = ''
    for s in str:
        result += int(iter)*s
    print(result)
