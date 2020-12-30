def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        result = ""
        temp = (bin(arr1[i] | arr2[i]))  # 이진수 and
        if (len(temp) < n + 2):  # 길이 부족한 수 -> 0 채우기
            tempzero = ""
            for j in range(n + 2 - len(temp)):
                tempzero += "0"
            temp = temp[0:2] + tempzero + temp[2:]
        for j in range(2, len(temp)):  # #과 공백으로 구성
            if (temp[j] == "1"):
                result += "#"
            else:
                result += " "
        answer.append(result)
    return answer