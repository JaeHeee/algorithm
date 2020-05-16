data = [1,10,5,8,7,6,4,3,2,9]
print(data)

def quickSort(data, start, end):
    # 원소가 1개인 경우
    if start >= end:
        return
    # 키는 첫번째 원소
    key = start
    i = start + 1
    j = end
    # 엇갈릴 때 까지 반복
    while i <= j:
        # 키 값보다 큰 값을 만날 때 까지 이동
        while i <= end and data[i] <= data[key]:
            i += 1
        # 키 값보다 작은 값을 만날 때 까지 이동
        while data[j] >= data[key] and j > start:
            j -= 1
        # 엇갈린 상태면 키 값과 교체
        if i > j:
            data[key], data[j] = data[j], data[key]
        else:
            data[i], data[j] = data[j], data[i]

    quickSort(data, start, j - 1)
    quickSort(data, j + 1, end)


quickSort(data, 0, 9)
print(data)