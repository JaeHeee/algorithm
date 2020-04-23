T = int(input())

def dp(n):
    d = []

    if n == 10:
        d.append(1)
        return d[-1]
    if n == 20:
        d.append(3)
        return d[-1]
    if len(d) == (n // 10):
        return d[n//10-1]
    return dp(n-10) + 2*dp(n-20)

for i in range(T):
    N = int(input())

    result = dp(N)

    print("#%d %s" % (i+1, result))
