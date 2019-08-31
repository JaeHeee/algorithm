#tournament

N, player1, player2 = map(int,input('').split())

def next(player):
    if player%2==0:
        player = player//2
        return player
    else:
        player = player//2 + 1
        return player

def game(N,player1,player2):
    round = 0
    if N == 1:
        round = -1
        return round
    else:
        if player1>N or player2 >N:
            round = -1
            return round
        else:
            while True:
                round += 1
                if (player1-player2==1 and player1%2==0) or (player1-player2==-1 and player2%2==0):
                    break
                else:
                    player1 = next(player1)
                    player2 = next(player2)
            return round

print(game(N,player1,player2))
