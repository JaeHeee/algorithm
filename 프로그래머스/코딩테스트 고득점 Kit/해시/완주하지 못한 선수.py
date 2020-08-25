def solution(participant, completion):
    answer = ''
    participant_d = {}

    # participant 의 원소들에 대해서 dictionary를 만듭니다.
    for p in participant:
        if p in participant_d.keys():
            participant_d[p] += 1
        else:
            participant_d[p] = 1

    # completion의 원소들을 이용해서 dictionary에서 완주한 선수들을 제거합니다.
    for c in completion:
        participant_d[c] -= 1
        if participant_d[c] == 0:
            participant_d.pop(c)

    answer = list(participant_d.keys())

    return answer[-1]