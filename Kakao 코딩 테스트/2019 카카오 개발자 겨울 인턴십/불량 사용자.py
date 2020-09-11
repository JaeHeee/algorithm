check_list = []


def check(idx, candidate, banned, length):
    global check_list
    # banned가 다 채워진 경우
    if idx == len(candidate):
        ban = set(banned)
        if len(ban) == length and ban not in check_list:
            check_list.append(ban)
        return
    # 재귀를 이용하여 banned를 계속 추가
    for u_id in candidate[idx]:
        if u_id not in banned:
            banned.append(u_id)
            check(idx + 1, candidate, banned, length)
            banned.remove(u_id)


def solution(user_id, banned_id):
    answer = 0
    candidate = []

    for b in banned_id:
        temp = set()
        for u in user_id:
            # 아이디의 길이를 먼저 확인
            if len(u) == len(b):
                check_count = 0
                # 매칭이 되는지 확인
                for u_word, b_word in zip(u, b):
                    if u_word == b_word or b_word == '*':
                        check_count += 1
                    else:
                        break
                # 매칭이 되면 temp에 추가
                if check_count == len(u):
                    temp.add(u)
        candidate.append(temp)

    check(0, candidate, [], len(banned_id))
    answer = len(check_list)
    print("answer:",answer)
    return answer
