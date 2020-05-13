def solution(dirs):
    answer = 0
    row_line = [[0]*11 for i in range(11)]
    col_line = [[0]*11 for i in range(11)]
    pos = [0, 0]
    dx_dy = {
        'L' : -1,
        'R' : 1,
        'D' : -1,
        'U' : +1
    }
    
    for d in dirs:
        if d == 'L' or d == 'R':
            if  -5 <= pos[0] + dx_dy[d] <= 5:
                pos[0] += dx_dy[d]
                if d == 'L' and row_line[5-pos[1]][pos[0]+5] ==0:
                    row_line[5-pos[1]][pos[0]+5] = 1
                elif d == 'R' and row_line[5-pos[1]][4+pos[0]] ==0:
                    row_line[5-pos[1]][pos[0]+4] = 1
        else:
            if  -5 <= pos[1] + dx_dy[d] <= 5:
                pos[1] += dx_dy[d]
                if d == 'U' and col_line[5-pos[1]][pos[0]+5] == 0:
                    col_line[5-pos[1]][pos[0]+5] = 1
                elif d == 'D' and col_line[4-pos[1]][pos[0]+5] == 0:
                    col_line[4-pos[1]][pos[0]+5] = 1
                    
    for c in col_line:
        answer += sum(c)
    
    for r in row_line:
        answer += sum(r)
        
    return answer
