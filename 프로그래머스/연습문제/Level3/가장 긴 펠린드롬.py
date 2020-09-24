import sys

sys.setrecursionlimit(10 ** 5)

# 팰린드롬 확인
def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


def solution(s):
    for cut in range(len(s), 0, -1):
        for start in range(0, len(s)):
            if start + cut > len(s):
                break

            cutStr = s[start:start + cut]

            if palindrome(cutStr) == True:
                return len(cutStr)