def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [c.lower() for c in cities]

    if cacheSize != 0:
        for c in cities:
            if c in cache:
                cache.pop()
    for c in cities:
        if c.lower() in cache:
            answer += 1
        else:
            cache.append(c.lower())
            answer += 5

        if len(cache) > cacheSize and cacheSize > 0:
            cache.pop(0)
    else:
        answer = len(cities) * 5
    return answer