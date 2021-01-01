from itertools import permutations


def solution(numbers):
    answer = ''
    temp = []
    temp = list(permutations(numbers, len(numbers)))

    result = []
    for i in range(len(temp)):
        tempresult = ""
        for j in range(len(temp[i])):
            tempresult += str(temp[i][j])
        result.append(int(tempresult))
    answer = str(max(result))

    return answer