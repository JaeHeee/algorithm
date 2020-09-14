import re

def solution(word, pages):
    webpages = []
    link_list = []
    link_count = {}
    link_score = {}
    basic_score = {}
    score = {}
    max_ = -1
    idx = -1
    count = 0

    for page in pages:
        # url 저장
        url = re.findall('<meta property="og:url" content="https://(.*)"/>', page)[0]
        webpages.append(url)

        # link 저장
        links = page.split('a href=\"https://')[1:]
        for link in links:
            link_list.append((url, link.split('"')[0]))

        # 링크 갯수, 기본 점수 저장
        link_count[url] = len(links)
        basic_score[url] = re.sub('[^a-zA-Z]', '.', page.lower()).split('.').count(word.lower())

    # 링크 점수 계산
    for url, link in link_list:
        if link in link_score:
            link_score[link] += basic_score[url] / link_count[url]
        else:
            link_score[link] = basic_score[url] / link_count[url]

    # 매칭 점수 계산
    for url in basic_score:
        score[url] = basic_score[url]
    for url in link_score:
        if url in score:
            score[url] += link_score[url]

    for url in webpages:
        if score[url] > max_:
            max_ = score[url]
            idx = count
        count += 1

    return idx