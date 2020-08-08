def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [c.lower() for c in cities]

    if cacheSize != 0:
        for c in cities:
            if c in cache:
                cache.pop(cache.index(c))
                cache.append(c)
                answer += 1
            else:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                    cache.append(c)
                else:
                    cache.append(c)
                answer += 5
    else:
        answer = len(cities) * 5

    return answer