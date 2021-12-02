def solution(m, musicinfos):
    answer = ''

    arr = []
    for i in musicinfos:
        temp = i.split(',')
        start = temp[0].split(':')  # 음악 시작 시간
        end = temp[1].split(':')  # 음악 끝난 시각
        min = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])  # 음악 재생 시간

        result = ''
        for j in range(len(temp[3])):  # ,와 공백으로 악보 구분
            if j != len(temp[3]) - 1 and temp[3][j + 1] != '#':
                result += temp[3][j] + ', '
            else:
                if j == len(temp[3]) - 1:
                    result += temp[3][j] + ','
                else:
                    result += temp[3][j]
        k = result.split(' ')

        music = (min // len(k)) * k + k[:(min % len(k))]  # 재생 시간 만큼 악보 그리기
        music = ' '.join(music)

        arr.append([min, temp[2], music])  # list: 재생 시간, 음악 제목, 악보

    result = ''
    for i in range(len(m)):  # ,와 공백으로 자신이 기억하는 멜로디 구분
        if i != len(m) - 1 and m[i + 1] != '#':
            result += m[i] + ', '
        else:
            result += m[i]
    result += ','

    mmax = -1
    for i in arr:  # 조건과 일치하는 음악 제목 찾기
        if result in i[2]:
            if mmax < i[0]:
                mmax = i[0]
                answer = i[1]

    if answer == '':  # 조건이 일치하는 음악이 없는 경우
        answer = '(None)'

    return answer