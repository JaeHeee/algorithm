T = int(input())

for i in range(T):
    count = int(input())
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    color1 = []
    color2 = []
    purple = 0

    for j in range(count):
        color_input = list(map(int,input().split()))

        if(color_input[-1] == 1):
            color1.append(color_input[:4])
        else:
            color2.append(color_input[:4])

    for color in color1:
        for k in range(color[0],color[2]+1):
            for l in range(color[1],color[3]+1):
                board[k][l] = 1

    for color in color2:
        for k in range(color[0],color[2]+1):
            for l in range(color[1],color[3]+1):
                if board[k][l]==1:
                    purple +=1

    print("#%d %d" % (i+1, purple))
