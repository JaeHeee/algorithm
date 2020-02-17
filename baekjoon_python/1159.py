N = int(input(''))
players = []
lineUp = ''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(N):
    player = input('')
    players.append(player[0])
    
players.sort()

for a in alphabet:
    if(players.count(a) >= 5):
        lineUp += a

if(len(lineUp)==0):
    print('PREDAJA')
else:
    print(lineUp)
