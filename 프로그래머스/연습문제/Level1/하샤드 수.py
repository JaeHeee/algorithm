def solution(x):
    number = 0
    n_length = len(str(x))
    temp = x

    for i in range(n_length):
        number += temp % 10
        temp //= 10

    if x % number:
        return False
    else:
        return True