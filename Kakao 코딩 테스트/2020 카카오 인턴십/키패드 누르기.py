def solution(numbers, hand):
    answer = ''
    left_side = [1, 4, 7, '*']
    right_side = [3, 6, 9, '#']
    center = [2, 5, 8, 0]
    pos_l = '*'
    pos_r = '#'
    # 손가락이 가운데에 있으면 True
    c_l = False
    c_r = False

    for n in numbers:
        if n in left_side:
            answer += 'L'
            pos_l = n
            c_l = False
        elif n in right_side:
            answer += 'R'
            pos_r = n
            c_r = False
        else:
            if c_l:
                l_dist = abs(center.index(n) - center.index(pos_l))
            else:
                l_dist = abs(center.index(n) - left_side.index(pos_l)) + 1

            if c_r:
                r_dist = abs(center.index(n) - center.index(pos_r))
            else:
                r_dist = abs(center.index(n) - right_side.index(pos_r)) + 1

            if l_dist < r_dist:
                pos_l = n
                c_l = True
                answer += 'L'
            elif l_dist > r_dist:
                pos_r = n
                c_r = True
                answer += 'R'
            else:
                if hand == 'left':
                    pos_l = n
                    c_l = True
                    answer += 'L'
                else:
                    pos_r = n
                    c_r = True
                    answer += 'R'

    return answer