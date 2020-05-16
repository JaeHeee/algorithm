sorted_data = [0]*8
numbers = [7,6,5,8,3,5,9,1]

def merge(data, m, middle, n):
    i = m
    j = middle + 1
    k = m
    # 작은 순서대로 배열에 삽입
    while i <= middle and j <= n:
        if data[i] <= data[j]:
            sorted_data[k] = data[i]
            i += 1
        else:
            sorted_data[k] = data[j]
            j +=1
        k += 1
    #남은 데이터도 삽입
    if i > middle:
        for t in range(j,n+1):
            sorted_data[k] = data[t]
            k += 1
    else:
        for t in range(i,middle+1):
            sorted_data[k] = data[t]
            k += 1

    for t in range(m,n+1):
        data[t] = sorted_data[t];

def mergeSort(data, m, n):
    if m < n:
        middle = (m + n) // 2
        mergeSort(data, m, middle)
        mergeSort(data, middle + 1, n)
        merge(data, m, middle, n)



mergeSort(numbers, 0, 7)
print(numbers)