def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        num = absolutes[i]

        if signs[i] == False:  # 음수일때
            answer -= num
        else:  # 양수일때
            answer += num

    return answer