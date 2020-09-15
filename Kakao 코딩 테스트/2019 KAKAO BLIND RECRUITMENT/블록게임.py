checked = set()

# 지울 수 있는 블럭 5가지 종류 찾아내기
def possible_block(board, i, j):
    try:
        if board[i + 1][j] == board[i][j] and \
                board[i + 1][j + 1] == board[i][j] and \
                board[i + 1][j + 2] == board[i][j]:
            return ((i, j + 1), (i, j + 2), board[i][j])
    except:
        pass
    try:
        if board[i + 1][j] == board[i][j] and \
                board[i + 2][j] == board[i][j] and \
                board[i + 2][j - 1] == board[i][j]:
            return ((i, j - 1), (i + 1, j - 1), board[i][j])
    except:
        pass
    try:
        if board[i + 1][j] == board[i][j] and \
                board[i + 2][j] == board[i][j] and \
                board[i + 2][j + 1] == board[i][j]:
            return ((i, j + 1), (i + 1, j + 1), board[i][j])
    except:
        pass
    try:
        if board[i + 1][j] == board[i][j] and \
                board[i + 1][j - 1] == board[i][j] and \
                board[i + 1][j - 2] == board[i][j]:
            return ((i, j - 1), (i, j - 2), board[i][j])
    except:
        pass
    try:
        if board[i + 1][j - 1] == board[i][j] and \
                board[i + 1][j] == board[i][j] and \
                board[i + 1][j + 1] == board[i][j]:
            return ((i, j - 1), (i, j + 1), board[i][j])
    except:
        pass

    return None

# 찾아낸 지울 수 있는 블럭 리스트에 넣기
def preprocess(board):
    list_ = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0 and board[i][j] not in checked:
                checked.add(board[i][j])
                type_ = possible_block(board, i, j)
                if type_ != None:
                    list_.append(type_)
    return list_

# 위쪽에 블럭이 존재하는지 확인
def head_check(board, i, j):
    for a in range(i + 1):
        if board[a][j] != 0:
            return True
    return False

# 블럭 제거
def remove(board, k):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == k:
                board[i][j] = 0


removed = set()


def solution(board):
    answer = 0
    possible_list = preprocess(board)

    while True:
        check = False
        for i in possible_list:
            black_x_1, black_y_1 = i[0]
            black_x_2, black_y_2 = i[1]
            k = i[2]

            if k in removed:
                continue

            if not head_check(board, black_x_1, black_y_1) and \
                    not head_check(board, black_x_2, black_y_2):
                removed.add(k)
                remove(board, k)
                check = True
                answer += 1

        if check is False:
            break

    return answer