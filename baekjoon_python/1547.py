#ball

M = int(input())
ball = [1,2,3]

def shift(cup1,cup2,ball):
    x = ball.index(cup1)
    y = ball.index(cup2)
    ball[x],ball[y] = ball[y],ball[x]

for i in range(M):
    cup1, cup2 = map(int,input().split(' '))
    shift(cup1, cup2,ball)


print(ball[0])
