def solution(n):
    strtemp = ''
    while (1):
        strtemp += str(n % 3)
        n = n // 3
        if (n == 0):
            break
    strtemp = strtemp[::-1]

    temp = 1
    answer = 0
    for i in range(len(strtemp)):
        answer += temp * int(strtemp[i])
        temp = temp * 3
    return answer