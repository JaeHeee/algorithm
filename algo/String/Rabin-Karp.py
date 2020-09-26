# 해시기법 사용
# 해시 : 긴 데이터를 그것을 상징하는 짧은 데이터로 바꿔주는 기법
# 각 문자의 아스키 코드 값에 2의 제곱수를 차례대로 곱하여 더해줘서 해시값을 계산
# 해시 값이 일치할 때 부분문자열과 매칭하여 검사
# 긴 글 해시 값 = 2*(긴글 해시값 - 가장 앞에 있는 문자의 수치) + 새롭게 들어온 문자의 수치


def rabinKarp(parent, pattern):
    parent_size = len(parent)
    pattern_size = len(pattern)
    parentHash = 0
    patternHash = 0
    power = 1

    for i in range(parent_size-pattern_size+1):
        if i == 0:
            for j in range(pattern_size):
                parentHash = parentHash + ord(parent[pattern_size-1-j])*power
                patternHash = patternHash + ord(pattern[pattern_size-1-j])*power

                if j < pattern_size - 1:
                    power *=2
        else:
            parentHash = 2*(parentHash-ord(parent[i-1])*power)+ord(parent[pattern_size-1+i])

        if parentHash == patternHash:
            finded = True
            for j in range(pattern_size):
                if parent[i+j] != pattern[j]:
                    finded = False
                    break

            if finded:
                print(i+1, "번째")


parent = "ababacabacaabacaaba"
pattern = "abacaaba"

rabinKarp(parent, pattern)