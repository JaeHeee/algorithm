N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

check = False
def binarySearch(start, end, target):
    global check
    if start > end:
        return
    mid = (start+end)//2
    if A[mid] == target:
        check = True
    elif A[mid] > target:
        return binarySearch(start, mid-1, target)
    else:
        return binarySearch(mid+1, end, target)

for b in B:
    check = False
    binarySearch(0, N-1, b)
    if check:
        print(1)
    else:
        print(0)
