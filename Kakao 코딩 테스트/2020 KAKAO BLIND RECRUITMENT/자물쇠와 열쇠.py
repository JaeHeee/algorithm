def rotate_ninety(key):
    new_key = []

    for i in range(len(key)):
        new_key.append([])
        for j in range(len(key) - 1, -1, -1):
            new_key[i].append(key[j][i])

    return new_key


def split_lock(lock, i, j, size):
    sub_lock = []
    idx = 0

    for m in range(i, i+size):
        sub_lock.append([])
        for n in range(j, j+size):
            sub_lock[idx].append(lock[m][n])
        idx+=1

    return sub_lock



def find_sol(key, sub_lock):
    check = True

    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == sub_lock[i][j]:
                return False

    return check


def convolution(key, lock):
    check = False

    for i in range(len(lock) - len(key) + 1):
        for j in range(len(lock) - len(key) + 1):
            if find_sol(key, split_lock(lock, i, j, len(key))):
                return True

    return check


def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)

    new_lock = [[1] * (M - 1) + l + [1] * (M - 1) for l in lock]
    new_lock = [[1] * (N + 2 * (M - 1))] * (M - 1) + new_lock + [[1] * (N + 2 * (M - 1))] * (M - 1)

    if convolution(key, new_lock):
        return True

    for i in range(3):
        new_key = rotate_ninety(key)
        if convolution(new_key, new_lock):
            return True

    return answer

