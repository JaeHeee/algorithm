# C 와 C# 처럼 겹치는 경우 발생하는 것 방지
def change(musics):
    musics = musics.replace('C#', 'c')
    musics = musics.replace('D#', 'd')
    musics = musics.replace('F#', 'f')
    musics = musics.replace('G#', 'g')
    musics = musics.replace('A#', 'a')
    return musics


def solution(m, musicinfos):
    name_list = []
    m = change(m)
    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = change(musicinfo)
        music = musicinfo.split(',')
        # 총 시간 계산
        start_time = music[0].split(':')
        end_time = music[1].split(':')
        time = (int(end_time[0]) * 60 + int(end_time[1])) - (int(start_time[0]) * 60 + int(start_time[1]))

        # 들은 멜로디 m이 방송에서 나온 곡과 일치하는지 확인
        if len(music[3]) >= time:
            melody = music[3][:time]
            if m in melody:
                name_list.append([idx, time, music[2]])
        else:
            melody = music[3] * (time // len(music[3])) + music[3][:time % len(music[3])]
            if m in melody:
                name_list.append([idx, time, music[2]])

    name_list.sort(key=lambda x: (-x[1], x[0]))

    if name_list:
        return name_list[0][2]
    else:
        return '(None)'