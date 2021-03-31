def solution(clothes):
    answer = 1

    temp = [[clothes[0][1], clothes[0][0]]]
    for i in range(1, len(clothes)):
        count = 0
        for j in range(len(temp)):
            if (temp[j][0] == clothes[i][1]):  # clothes 같은 종류라면
                temp[j].append(clothes[i][0])
                break
            else:
                count += 1
        if (count == len(temp)):  # 끝까지 돌았는데 같은 종류가 없다면 추가
            temp.append([clothes[i][1], clothes[i][0]])

    # (갯수+1) * (갯수 +1) -1
    # +1을 해주는 이유는 안입는 경우를 위하여 +1을 해줌
    # -1을 해주는 이유는 아무것도 안입는 경우를 위하여 -1을 해줌

    for i in range(len(temp)):
        answer *= len(temp[i])

    return answer - 1