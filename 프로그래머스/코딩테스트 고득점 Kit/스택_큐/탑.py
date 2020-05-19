def solution(heights):
    answer = [0]
    for i in range(1, len(heights)):
        check = 0
        for j in range(i - len(heights) - 1, -len(heights) - 1, -1):
            if heights[j] > heights[i]:
                answer.append(j + len(heights) + 1)
                check = 1
                break
        if check == 0:
            answer.append(0)

    return answer