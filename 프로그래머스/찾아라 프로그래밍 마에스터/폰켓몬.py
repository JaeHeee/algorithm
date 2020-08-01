def solution(nums):
    monster = len(nums) // 2
    counts = [0] * 200001

    for n in nums:
        counts[n] += 1

    check = 200001 - counts.count(0)

    if monster <= check:
        return monster
    else:
        return check