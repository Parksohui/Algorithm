def solution(numbers, hand):
    answer = ''
    tempR = 12
    tempL = 10

    for i in range(len(numbers)):
        if (numbers[i] == 0):
            numbers[i] = 11
        if (numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7):
            answer += "L"
            tempL = numbers[i]
        elif (numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9):
            answer += "R"
            tempR = numbers[i]
        else:
            temp1 = abs(numbers[i] - tempL)
            temp2 = abs(numbers[i] - tempR)
            dstL = 0
            dstR = 0
            if (temp1 == 1 or temp1 == 3):
                dstL = 1
            elif (temp1 == 2 or temp1 == 4 or temp1 == 6):
                dstL = 2
            elif (temp1 == 5 or temp1 == 7 or temp1 == 9):
                dstL = 3
            elif (temp1 == 8 or temp1 == 10):
                dstL = 4

            if (temp2 == 1 or temp2 == 3):
                dstR = 1
            elif (temp2 == 2 or temp2 == 4 or temp2 == 6):
                dstR = 2
            elif (temp2 == 5 or temp2 == 7 or temp2 == 9):
                dstR = 3
            elif (temp2 == 8 or temp2 == 10):
                dstR = 4

            if (dstL < dstR):
                answer += "L"
                tempL = numbers[i]
            elif (dstL == dstR):
                if (hand == "right"):
                    answer += "R"
                    tempR = numbers[i]
                else:
                    answer += "L"
                    tempL = numbers[i]
            else:
                answer += "R"
                tempR = numbers[i]

    return answer