def solution(clothes):
    answer = 0

    temp = [[clothes[0][1], clothes[0][0]]]
    for i in range(1, len(clothes)):
        count = 0
        for j in range(len(temp)):
            if (temp[j][0] == clothes[i][1]):
                temp[j].append(clothes[i][0])
                break
            else:
                count += 1
        if (count == len(temp)):
            temp.append([clothes[i][1], clothes[i][0]])

    print(temp)

    answer += len(temp[0]) - 1

    if (len(temp) != 1):
        multi = len(temp[0]) - 1
        for i in range(1, len(temp)):
            answer += len(temp[i]) - 1
            multi *= len(temp[i]) - 1
        answer += multi

    return answer