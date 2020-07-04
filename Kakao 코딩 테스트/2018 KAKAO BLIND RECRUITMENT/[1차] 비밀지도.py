def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        binary = format(i | j, 'b')
        binary = '0' * (n - len(binary)) + binary
        result = ''
        for b in binary:
            if b == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)
    return answer