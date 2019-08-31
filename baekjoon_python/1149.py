#RGB Street

N = int(input(''))
rgb = []

for i in range(N):
    r,g,b = map(int,input('').split())
    rgb.append([r,g,b])

def RGB(N):
    if N==0:
        return [0,0,0]
    elif N==1:
        return rgb[0]
    else:
        for i in range(N-1):
            memo = rgb[i]
            rgb[i+1][0] += min(memo[1],memo[2])
            rgb[i+1][1] += min(memo[0],memo[2])
            rgb[i+1][2] += min(memo[0],memo[1])
        return rgb[N-1]


print(min(RGB(N)))
