def solution(phone_number):
    answer = phone_number.replace(phone_number[:len(phone_number)-4],'*'*(len(phone_number)-4))
    return answer