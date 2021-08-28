def solution(arr1, arr2):
    answer = []

    k = 0
    for i in range(len(arr1)): #A*B, C*D => (B==C)
        val = []
        for j in range(len(arr2[0])):
            temp = 0
            while (k < len(arr2)):
                temp += (arr1[i][k] * arr2[k][j])
                k += 1
                if k >= len(arr2):
                    k = 0
                    val.append(temp)
                    break
        answer.append(val)

    return answer