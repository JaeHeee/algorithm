def solution(phone_book):
    answer = True
    for p in phone_book:
        for h in phone_book:
            if p==h:
                continue
            if h[:len(p)] == p:
                return False
    return answer