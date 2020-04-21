T = int(input())

for i in range(T):
    word_board = []
    word_board_col = []
    N, M = map(int, input().split())

    for n in range(N):
        word_board.append(input())
        word_board_col.append('')

    for w_row in word_board:
        for m in range(N-M+1):
            if w_row[m:m+M] == w_row[m+M-N-1:m-N-1:-1]:
                palindrome = w_row[m:m+M]
        for n in range(N):
            word_board_col[n] += w_row[n]

    for w_col in word_board_col:
        for m in range(N - M + 1):
            if w_col[m:m + M] == w_col[m+M-N-1:m-N-1:-1]:
                palindrome = w_col[m:m + M]

    print("#%d %s" % (i+1, palindrome))
