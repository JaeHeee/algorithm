def solution(genres, plays):
    answer = []
    genres_play = {}
    for genre, play in zip(genres, plays):
        if genre in genres_play.keys():
            genres_play[genre] += play
        else:
            genres_play[genre] = play

    genre_rank = [genre for genre, play in sorted(genres_play.items(), key=lambda x: x[1], reverse=True)]

    index_g_p = {(g_p[0], i): g_p[1] for i, g_p in enumerate(zip(genres, plays))}

    i_rank = [g_i for g_i, play in sorted(index_g_p.items(), key=lambda x: x[1], reverse=True)]

    for gr in genre_rank:
        count = 0
        for k in i_rank:
            if count == 2:
                break
            if gr in k:
                answer.append(k[1])
                count += 1

    return answer