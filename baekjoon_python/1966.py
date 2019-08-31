#printer queue

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    printer = list(map(int,input().split()))
    number = 1
    while True:
        if M==0 and max(printer) == printer[M]:
            print(number)
            break
        elif M==0 and max(printer) != printer[M]:
            printer.append(printer[M])
            del printer[0]
            M = len(printer)-1
        elif M!=0 and max(printer) == printer[0]:
            del printer[0]
            M -= 1
            number+=1
        elif M!=0 and max(printer) != printer[0]:
            printer.append(printer[0])
            del printer[0]
            M -= 1
