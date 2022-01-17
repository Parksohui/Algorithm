def solution(id_list, report, k):
    answer = [0] * len(id_list)

    dict = {}  # 유저ID : 유저가 신고한 ID
    for i in id_list:  # 초기화
        dict[i] = []

    for i in report:  # dict로 정리
        x = i.split()
        dict[x[0]].append(x[1])

    for key, value in dict.items():  # 동일 유저에 대한 신고 횟수는 1회로 처리
        dict[key] = set(value)

    temp = {}  # 신고된 ID: 신고된 횟수
    for i in id_list:  # 초기화
        temp[i] = 0

    for key, value in dict.items():  # 신고
        for i in value:
            temp[i] += 1

    for key, value in temp.items():
        if value >= k:  # k번 이상 신고된 유저
            for x, y in dict.items():
                if key in y:  # 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
                    answer[id_list.index(x)] += 1

    return answer