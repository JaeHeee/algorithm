#Josephus problem

N ,M = map(int,input('').split())

queue = []

for i in range(1,N+1):
    queue.append(i)

print("<",end='')
while len(queue) != 0:
    if len(queue) == 1:
        print(queue[0],end='')
        print(">")
        break
    if len(queue)<=M:
        for i in range(1,M):
            queue.append(queue[0])
            del queue[0]
        print(queue[0],end=', ')
        del queue[0]
    if len(queue)>M:
        queue.extend(queue[:M-1])
        del queue[:M-1]
        print(queue[0],end=', ')
        del queue[0]
