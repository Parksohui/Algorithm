def solution(answers):
    answer = []

    A = [1, 2, 3, 4, 5]
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    length = len(answers)

    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(length):
        if (answers[i] == A[i % len(A)]):
            count1 += 1
        if (answers[i] == B[i % len(B)]):
            count2 += 1
        if (answers[i] == C[i % len(C)]):
            count3 += 1
    result = []

    answer.append(count1)
    result.append(1)
    if (answer[0] < count2):
        answer.clear()
        result.clear()
        answer.append(count2)
        result.append(2)
    elif (answer[0] == count2):
        answer.append(count2)
        result.append(2)
    if (answer[0] < count3):
        answer.clear()
        result.clear()
        answer.append(count3)
        result.append(3)
    elif (answer[0] == count3):
        answer.append(count3)
        result.append(3)

    return result