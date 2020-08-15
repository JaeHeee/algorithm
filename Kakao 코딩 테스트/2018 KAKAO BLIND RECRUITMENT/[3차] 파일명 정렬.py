def solution(files):
    data = []

    for idx, file in enumerate(files):
        data.append([])
        name = ''
        num = ''
        for f in file:
            if f.isdigit() and len(data[idx]) < 2:
                if name:
                    data[idx].append(name)
                    name = ''
                num += f
            else:
                if num:
                    data[idx].append(num)
                    num = ''
                name += f
        if name:
            data[idx].append(name)
        if num:
            data[idx].append(num)

    data.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = ["".join(file) for file in data]

    return answer