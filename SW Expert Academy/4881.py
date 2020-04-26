T = int(input())


def finder(n, current_row, current_candidate):
    global temp, result
    
    if temp > result:
        return 

    if current_row == n:
        if temp < result:
            result = temp
        return

    for candidate_col in range(n):
        if not current_candidate[candidate_col]:
            current_candidate[candidate_col] = 1
            temp += numbers[candidate_col][current_row]
            finder(n, current_row + 1, current_candidate)
            current_candidate[candidate_col] = 0
            temp -= numbers[candidate_col][current_row]


for i in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for i in range(N)]

    temp, result = 0, 31
    finder(N, 0, [0]*N)

    print("#%d %d" % (i + 1, result))
