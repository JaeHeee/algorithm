def solution(files):
    data = []

    for idx, file in enumerate(files):
        data.append([])
        name = ''
        num = ''
        for f in file:
            # 이미 숫자가 data에 들어간 경우 그 이후로 나오는 숫자는 문자로 취급
            if f.isdigit() and len(data[idx]) < 2:
                # data에 name 추가
                if name:
                    data[idx].append(name)
                    name = ''
                num += f
            else:
                # data에 num 추가
                if num:
                    data[idx].append(num)
                    num = ''
                # 문자면 name에 추가
                name += f
        # 확장자명 추가
        if name:
            data[idx].append(name)
        if num:
            data[idx].append(num)

    # 기준에 맞게 정렬
    data.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = ["".join(file) for file in data]

    return answer