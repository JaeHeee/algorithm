numbers = list(map(int,input('').split()))
six=0

for n in numbers:
    six += n*n
    
print(six%10)
