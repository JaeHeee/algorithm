def four_block(row, col, board):
    idx = []
    blocks = set()
    if board[row][col] == 0 or board[row][col + 1] == 0 or board[row + 1][col] == 0 or board[row + 1][col + 1] == 0:
        return idx

    for i in range(row, row + 2):
        for j in range(col, col + 2):
            idx.append([i, j])
            blocks.add(board[i][j])

    if len(blocks) == 1:
        return idx
    else:
        return []


def remove_block(idx, board):
    for i, j in idx:
        board[i][j] = 0
        if board[i - 1][j] != 0:
            k = i
            while k > 0:
                board[k][j], board[k - 1][j] = board[k - 1][j], board[k][j]
                k -= 1

    if idx:
        return True
    else:
        return False


def solution(m, n, board):
    answer = 0
    check = True
    board = [list(b) for b in board]

    while check:
        idx = []
        for row in range(m - 1):
            for col in range(n - 1):
                block_idx = four_block(row, col, board)
                for b in block_idx:
                    idx.append(b)
        idx = list({(i, j) for i, j in idx})
        idx.sort(key=lambda x: (x[0], x[1]))
        answer += len(idx)
        check = remove_block(idx, board)

    return answer