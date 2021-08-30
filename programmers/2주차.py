def solution(scores):
    answer = ''

    avgtemp = []
    for j in range(len(scores)): # 열에 따라 list
        arr = []
        for i in range(len(scores)):
            arr.append(scores[i][j])
        avgtemp.append(arr)

    # 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구하기
    result = []
    for i in range(len(avgtemp)):
        temp = avgtemp[i]
        sumavg = sum(temp)
        if temp.count(min(temp)) == 1 and min(temp) == temp[i]:
            sumavg -= min(temp)
            avg = sumavg / (len(temp) - 1)
        elif temp.count(max(temp)) == 1 and max(temp) == temp[i]:
            sumavg -= max(temp)
            avg = sumavg / (len(temp) - 1)
        else:
            avg = sumavg / len(temp)

        score = ''
        if avg >= 90:
            score = 'A'
        elif avg >= 80 and avg < 90:
            score = 'B'
        elif avg >= 70 and avg < 80:
            score = 'C'
        elif avg >= 50 and avg < 70:
            score = 'D'
        else:
            score = 'F'
        result.append(score)

    answer = ''.join(result)

    return answer