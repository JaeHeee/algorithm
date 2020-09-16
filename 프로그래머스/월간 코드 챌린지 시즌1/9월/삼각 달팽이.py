def solution(n):
    answer = []
    tri = [[] for _ in range(n)]

    left_count = n
    left_row = 0
    left_col = 0
    bottom_count = n - 1
    bottom_row = n - 1
    bottom_col = 1
    right_count = n - 2
    right_row = n - 2
    right_col = 0
    order = 0

    i = 1
    while i <= n * (n + 1) // 2:
        # 왼쪽 아래로 내려가는 경우
        if order == 0:
            for j in range(left_row, left_row + left_count):
                tri[j].insert(left_col, i)
                i += 1
            left_count -= 3
            left_row += 2
            left_col += 1
            order = 1
        # 가장 아래쪽에서 오른쪽으로 가는경우
        elif order == 1:
            data = []
            for num in range(i, i + bottom_count):
                data.append(num)
            i += bottom_count
            tri[bottom_row][:bottom_col] += data
            bottom_count -= 3
            bottom_row -= 1
            bottom_col += 1
            order = 2
        # 오른쪽 위로 올라가는 경우
        else:
            for j in range(right_row, right_row - right_count, -1):
                tri[j].insert(len(tri[j]) - right_col, i)
                i += 1
            right_count -= 3
            right_row -= 1
            right_col += 1
            order = 0

    for t in tri:
        answer += t

    return answer