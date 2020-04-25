T = int(input())


def finder(s):
    global result
    if maze[s[0]][s[1]] == 3 or result == 1:
        result = 1
        return

    stack.append([s[0], s[1]])
    t = [0, 0]
    for l in range(4):
        t[0] = s[0] + dx[l]
        t[1] = s[1] + dy[l]
        if 0 <= t[0] < N and 0 <= t[1] < N and \
                (maze[t[0]][t[1]] == 3 or maze[t[0]][t[1]] == 0)\
                and [t[0],t[1]] not in stack:
            finder(t)


for i in range(T):
    N = int(input())
    maze = [list(map(int, input())) for j in range(N)]
    stack = []
    result = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k, m in enumerate(maze):
        if 2 in m:
            s = [k, m.index(2)]

    finder(s)

    print("#%d %d" % (i + 1, result))

