def solution(arr1, arr2):
    answer = []
    arr1_row = len(arr1)
    arr1_col = len(arr1[0])
    arr2_row = len(arr2)
    arr2_col = len(arr2[0])

    for i in range(arr1_row):
        answer.append([])
        for j in range(arr2_col):
            answer[i].append(0)

    for i in range(arr1_row):
        for j in range(arr1_col):
            for k in range(arr2_col):
                answer[i][k] += (arr1[i][j] * arr2[j][k])

    return answer