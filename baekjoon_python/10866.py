#10866 Deque

count = int(input(''))
deque = []

for i in range(0,count):
    command= str(input(''))
    if "push_front" in command:
        number = int(command[10:])
        deque.insert(0,number)
    elif "push_back" in command:
        number = int(command[10:])
        deque.append(number)
    elif command == "pop_front":
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop(0))
    elif command == "pop_back":
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop())
    elif command == "size":
        print(len(deque))
    elif command == "empty":
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif command == "back":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])
