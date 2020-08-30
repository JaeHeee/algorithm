def solution(msg):
    answer = []
    word_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    max_ = 1
    pos = 0

    while pos < len(msg):
        for i in range(max_, 0, -1):
            if msg[pos:pos + i] in word_dict:
                answer.append(word_dict.index(msg[pos:pos + i]) + 1)
                # word_dict 에 새로운 단어 추가
                word_dict.append(msg[pos:pos + i + 1])
                pos += i
                # 새로운 단어의 길이를 확인해서 max 길이 업데이트
                max_ = max(len(msg[pos:pos + i + 1]), max_)
                break

    return answer