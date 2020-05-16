numbers = [1,3,5,7,9,11,14,15,18,19,25,28]

def binarySearch(start, end, target):
    if start > end:
        return
    mid = (start+end)//2
    if numbers[mid] == target:
        print(mid+1,"번")
    elif numbers[mid] > target:
        return binarySearch(start, mid-1, target)
    else:
        return binarySearch(mid+1, end, target)


binarySearch(0,len(numbers)-1,7)