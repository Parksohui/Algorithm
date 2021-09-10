def solution(genres, plays):
    answer = []

    dic = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] += plays[i]
    dic = sorted(dic.items(), key=lambda x: -x[1])  # 많이 재생된 장르 순

    temp = []
    for i in range(len(genres)):  # list: 장르, 재생 횟수, 고유 번호
        temp.append([genres[i], plays[i], i])

    temp.sort(key=lambda x: (x[0], -x[1]))  # 정렬: 장르 이름 순, 재생 횟수 순

    for i in range(len(dic)):  # 장르별로 2개씩 고유 번호 출력
        cnt = 0
        for j in range(len(temp)):
            if temp[j][0] == dic[i][0]:
                answer.append(temp[j][2])
                cnt += 1
            if cnt >= 2:
                break

    return answer