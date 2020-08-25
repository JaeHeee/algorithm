def solution(phone_book):
    answer = True
    
    # 전화번호를 잘라서 dictionary로 저장
    phone_book_d = { p:[p[:i+1]for i in range(len(p))] for p in phone_book}

    # 접두사로 존재하는지 확인
    for k in phone_book_d.keys():
        for v in phone_book_d.values():
            if v[-1] != k and k in v:
                return False

    return answer