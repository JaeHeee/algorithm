#AC

test = int(input(''))
results = []
for i in range(test):
    p = str(input(''))
    number = int(input(''))
    arr = (input(''))

    if arr[1]==']':
        ac_arr = []
    else:
        arr = arr[1:-1].split(',')
        ac_arr = []
        for i in range(len(arr)):
            ac_arr.append(int(arr[i]))

    if p.count('D')>len(ac_arr):
        results.append('error')
    else:
        direction = 0;
        c = 1
        for i in range(len(p)):
            if i == len(p)-1:
                if p[i]=='R':
                    ac_arr.reverse()
                else:
                    del ac_arr[direction]
            else:
                if p[i]=='R':
                    c *= -1
                    direction += c
                else:
                    del ac_arr[direction]
        if direction ==-1:
            ac_arr.reverse()
        results.append(ac_arr)

for result in results:
    print(str(result).replace(' ', ''))
