# stack sequence

count = int(input(""))
stack = []
sequence = []
result = []

for i in range(count):
    sequence.append(int(input("")))

index=0
for i in range(1,count+1):
    stack.append(i)
    result.append('+')
    while (len(stack)!=0) and (stack[-1] == sequence[index]):
        stack.pop()
        result.append('-')
        index +=1

if len(stack)!=0:
    print("NO")
else:
    for value in result:
        print(value)
