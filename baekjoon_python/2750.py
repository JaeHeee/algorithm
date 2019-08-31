count = int(input(""))
numbers = []
while 0 < count:
    number = int(input(""))
    numbers.append(number)
    count -= 1;
numbers.sort()
for i in numbers:
    print(i)
