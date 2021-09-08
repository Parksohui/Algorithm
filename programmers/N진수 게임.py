def solution(n, t, m, p):
    answer = ''

    tempstr = '0'
    i = 1
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}  # 10~15는 각각 대문자 A~F로 출력

    # n진법 구하기
    while True:
        temp = ''
        k = i
        while True:
            x, y = divmod(k, n)
            if y >= 10:  # 10 이상이면 A~F로 출력
                temp += dic[y]
            else:  # 나머지 문자열로 출력
                temp += str(y)
            k = x
            if x <= 0:  # 끝
                break
        i += 1
        tempstr += temp[::-1]  # 뒤집어서 추가
        if len(tempstr) >= (t * m):  # 자리수만큼
            break

    for i in range(len(tempstr)):  # 자기 차례에 말할 숫자
        if i % m == p - 1:
            answer += tempstr[i]
        if len(answer) == t:
            break

    return answer