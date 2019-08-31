#word master

word = input('')
word = word.upper()
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = []

for i in alphabet:
    numbers.append(word.count(i))

large_number = max(numbers)

if numbers.count(large_number)>1:
    print('?')
else:
    print(alphabet[numbers.index(large_number)])
