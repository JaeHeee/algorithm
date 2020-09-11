def four_block(row, col, board):
    idx = []
    blocks = set()
    # 해당 영역이 이미 제거되어 있는 경우
    if board[row][col] == 0 or board[row][col + 1] == 0 or board[row + 1][col] == 0 or board[row + 1][col + 1] == 0:
        return idx

    for i in range(row, row + 2):
        for j in range(col, col + 2):
            idx.append([i, j])
            blocks.add(board[i][j])

    if len(blocks) == 1: # 해당 영역의 블록이 모두 같은 경우
        return idx
    else:
        return []


def remove_block(idx, board):
    for i, j in idx:
        board[i][j] = 0
        # 지운 블럭위에 다른 블럭이 있는 경우
        if board[i - 1][j] != 0:
            k = i
            # 블럭을 아래로 내려준다.
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
        idx = list({(i, j) for i, j in idx}) # 중복되는 블럭 인덱스 제거
        idx.sort(key=lambda x: (x[0], x[1]))
        answer += len(idx) # 지워진 블럭 갯수 추가
        check = remove_block(idx, board)

    return answer
