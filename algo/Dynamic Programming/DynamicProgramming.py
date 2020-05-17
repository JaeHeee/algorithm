def fib(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if d[x]:
       return d[x]
    d.insert(x, fib(x - 1) + fib(x - 2))
    return d[x]

d = [0]*31
print(fib(30))