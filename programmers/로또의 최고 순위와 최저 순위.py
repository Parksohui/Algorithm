def solution(lottos, win_nums):
    answer = []

    match = []
    zero = 0
    for i in lottos:
        if i == 0:  # 알아 볼 수 없는 번호
            zero += 1
        else:
            for j in win_nums:
                if i == j:  # 일치하는 번호
                    match.append(i)

    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    answer.append(dic[len(match) + zero])  # 최고 순위
    answer.append(dic[len(match)])  # 최저 순위
    return answer