# BAEKJOON 로봇 청소기

n, m = map(int, input().split())
board = []
answer = 0

r, c, d = map(int, input().split(' '))
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
check = 0

for _ in range(n):
    line = list(map(int, input().split(' ')))
    board.append(line)

while True:
    # 현재 위치를 청소
    if board[r][c] == 0 :
        answer += 1
        board[r][c] = -1
    if d < 0:
        d += 4

    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
    if check == 4:
        if board[r+directions[d-2][0]][c+directions[d-2][1]] != 1:
            r += directions[d-2][0]
            c += directions[d-2][1]
            check = 0
        else:
            break

    # 왼쪽 방향으로 회전
    if board[r+directions[d-1][0]][c+directions[d-1][1]] == 0:
        d -= 1
        r += directions[d][0]
        c += directions[d][1]
        check = 0
    else:
        d -= 1
        check += 1

print(answer)
