def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    
    # 표의 값이 모두 0 인 경우 찾기
    for b in board:
        answer += sum(b)
    if answer == 0:
        return 0
    
    answer = 0
    for i in range(1, row):
        for j in range(1, col):
            # 왼쪽, 왼쪽 위, 위 3가지 값이 모두 0인 경우가 아니라면, 3가지 중 가장작은 값에 +1 한 값을 넣어준다.
            if board[i][j] == 0:
                continue
            else:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(board[i][j], answer)
    
    # 첫번째 행이나 열에 1이 있는 경우
    if answer == 0:
        return 1
    else:
        return answer**2