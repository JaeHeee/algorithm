#factorial

N = int(input())

if N<2:
    print(1)
else:
    result = 1
    for i in range(2,N+1):
        result = result*i
    print(result)
