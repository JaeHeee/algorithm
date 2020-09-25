# 회전 시키기
def rotate_ninety(key):
    new_key = []

    for i in range(len(key)):
        new_key.append([])
        for j in range(len(key) - 1, -1, -1):
            new_key[i].append(key[j][i])

    return new_key


# key 넣어보고 자물쇠와 맞으면 True
def find_sol(key, i, j, lock):

    for m in range(len(key)):
        for n in range(len(key)):
            lock[i+m][j+n] += key[m][n]

    for x in range(len(key)-1, len(lock)-len(key)+1):
        for y in range(len(key)-1, len(lock)-len(key)+1):
            if lock[x][y] != 1:
                return False
    return True


# key 다시 빼주기
def restore(key, i, j, lock):
    for m in range(len(key)):
        for n in range(len(key)):
            lock[i+m][j+n] -= key[m][n]


# 슬라이딩하면서 계산
def convolution(key, lock):
    check = False

    for i in range(len(lock) - len(key) + 1):
        for j in range(len(lock) - len(key) + 1):
            if find_sol(key, i, j, lock):
                return True
            restore(key, i, j, lock)

    return check


def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)

    # new_lock 0으로 채우기
    new_lock = [[0] * ((M-1) * 2 + N) for _ in range((M-1) * 2 + N)]
    for i in range(N):
        for j in range(N):
            new_lock[M-1 + i][M-1 + j] = lock[i][j]

    # 슬라이딩하면서 계산
    if convolution(key, new_lock):
        return True

    # 키 회전해서 계산
    new_key = key
    for i in range(3):
        new_key = rotate_ninety(new_key)
        if convolution(new_key, new_lock):
            return True

    return answer
