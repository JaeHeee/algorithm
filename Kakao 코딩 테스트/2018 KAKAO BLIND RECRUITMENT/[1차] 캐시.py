def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [c.lower() for c in cities]

    if cacheSize != 0:
        for c in cities:
            # cache에 이미 있는 경우 이미 있는 것 꺼내고 새로온 것 추가
            if c in cache:
                cache.pop(cache.index(c))
                cache.append(c)
                answer += 1
            else:
                # cache가 이미 꽉 찾으면 제일 오랜된 것 꺼내고 새로 추가
                if len(cache) >= cacheSize:
                    cache.pop(0)
                    cache.append(c)
                else:
                    cache.append(c)
                answer += 5
    # cacheSize가 0 이면 모두 cache miss(5)
    else:
        answer = len(cities) * 5

    return answer