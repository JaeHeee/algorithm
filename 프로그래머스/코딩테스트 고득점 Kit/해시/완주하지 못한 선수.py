def solution(participant, completion):
    completion.sort()
    participant.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[-1]