check_list = []


def check(idx, candidate, temp, length):
    global check_list
    if idx == len(candidate):
        if len(temp) == length and set(temp) not in check_list:
            check_list.append(set(temp))
        return

    for u_id in candidate[idx]:
        if u_id not in temp:
            temp.append(u_id)
            check(idx + 1, candidate, temp, length)
            temp.remove(u_id)


def solution(user_id, banned_id):
    answer = 0
    candidate = []

    for b in banned_id:
        temp = set()
        for u in user_id:
            if len(u) == len(b):
                check_count = 0
                for u_word, b_word in zip(u, b):
                    if u_word == b_word or b_word == '*':
                        check_count += 1
                    else:
                        break
                if check_count == len(u):
                    temp.add(u)
            if temp not in candidate:
                candidate.append(temp)

    check(0, candidate, [], len(banned_id))
    answer = len(check_list)
    return answer
